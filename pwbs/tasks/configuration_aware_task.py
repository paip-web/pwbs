# -*- coding: utf-8 -*-
"""PAiP Web Build System - Configuration Aware Task

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT
"""
# Imports
from abc import ABC
import sys
import sentry_sdk
from pwbs.runner.docker import DockerRunner
from pwbs.tasks.task import Task
from pwbs.core import service_manager
from pwbs.core import config_manager
from pwbs.tasks.task_constants import TaskConstants
from pwbs.core import UserError
from pwbs.core.error_messages import ErrorMessages

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class ConfigurationAwareTask(Task, ABC):
    """Configuration Aware Task Class"""

    def __init__(self, config=None):
        """
        Task Initialization Method
        """
        super().__init__(config)
        self.tmp_storage = {}

    @service_manager.inject('log')
    def before_execute(self, *args, log, **kwargs):
        """
        Before Task Execution Method
        Provide all params from execute method except services applied through service manager
        """
        # Extend Task Configuration
        self.config.extend_from_cli_arguments()
        # Run task in docker
        if self.config.docker and DockerRunner.is_it_docker() is False:
            docker_runner = DockerRunner()
            # Run single task in container
            pwbs_args = sys.argv[1:]
            parsed_args = config_manager['arguments']
            pwbs_task_found = False
            pwbs_args_wo_tasks = []
            for arg in pwbs_args:
                if arg in parsed_args.Task and pwbs_task_found is False:
                    pwbs_task_found = True
                    pwbs_args_wo_tasks.append(self.config.name)
                elif arg not in parsed_args.Task:
                    pwbs_args_wo_tasks.append(arg)
            docker_runner.execute(''.join(pwbs_args_wo_tasks))
            return False
        # Verbose Level and Debug Mode
        # # Save old values
        self.tmp_storage['debug'] = log.debug_state
        self.tmp_storage['verbose'] = log.verbose_state
        # # Prepare Overrides
        # # # If debug mode is on then it should be on
        debug_level = self.config.debug or self.tmp_storage['debug']
        # # # If verbose level is specified to debug mode then it should be on
        # # # Or when verbose level is not specified through task configuration
        verbose_level = self.config.verbose
        if self.tmp_storage['verbose'] == TaskConstants.task_verbose().debug() or self.config.verbose is None:
            verbose_level = self.tmp_storage['verbose']
        # # Override
        log.debug(debug_level)
        log.verbose(verbose_level)
        # Deprecated Task
        if self.config.deprecated:
            log.log_verbose('Task {} is deprecated!'.format(self.name), TaskConstants.task_verbose().normal())
        # Log Before
        log.log_verbose("Running {0} Task...".format(self.name), TaskConstants.task_verbose().normal())
        return True

    @service_manager.inject('log')
    def after_execute(self, *args, tasks, log, **kwargs):
        """
        After Task Execution Method
        Provide all params from execute method except services applied through service manager
        """
        # Execute Extended Tasks

        def task_extends(extends) -> None:
            """
            Extend Tasks
            :param extends: Extends
            """
            for task in extends:
                # Log Execute
                log.log_verbose('Executing "{0}"...'.format(task), TaskConstants.task_verbose().verbose())
                if task not in tasks:
                    raise UserError(ErrorMessages.task_not_found(task))
                tasks[task](*args, tasks=tasks, **kwargs)

        if self.config.extends != '' and self.config.extends is not None:
            if isinstance(self.config.extends, str):
                task_extends(self.config.extends.split(','))
            elif isinstance(self.config.extends, list):
                task_extends(self.config.extends)
        # Log Finish
        log.log_verbose("Finished {0} Task...".format(self.name), TaskConstants.task_verbose().normal())
        # Return to previous data for logger
        log.debug(self.tmp_storage['debug'])
        log.verbose(self.tmp_storage['verbose'])

    def __call__(self, *args, **kwargs):
        """
        Task Execution Method
        """
        self.process_config()
        with sentry_sdk.configure_scope() as scope:
            self.config.attach_to_sentry(scope)
        be = self.before_execute(*args, **kwargs)
        if be is True:
            self.execute(*args, **kwargs)
            self.after_execute(*args, **kwargs)
