# -*- coding: utf-8 -*-
"""PAiP Web Build System - MultiTask Mode

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from pwbs.tasks.configuration_aware_task import ConfigurationAwareTask
from pwbs.core import service_manager
from pwbs.tasks.task_factory import task_factory_map
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


class MultiTaskMode(ConfigurationAwareTask):
    """MultiTask Mode Class"""

    @staticmethod
    def init():
        """Initialize Task Mode"""
        task_factory_map[TaskConstants.task_mode().multi_task()] = MultiTaskMode

    @service_manager.inject('log')
    def execute(self, *args, tasks, log, **kwargs):
        """
        Task Execution Method
        """
        # Process Commands and their output

        def execute_command(task_name: str) -> None:
            """
            Execute Task
            :param str task_name: Task Name
            """
            # Log Execute
            log.log_verbose('Executing "{0}"...'.format(task_name), TaskConstants.task_verbose().verbose())
            if task_name not in tasks:
                raise UserError(ErrorMessages.task_not_found(task_name))
            tasks[task_name](*args, tasks=tasks, **kwargs)

        if isinstance(self.config.commands, str):
            execute_command(self.config.commands)
        elif isinstance(self.config.commands, list):
            for task in self.config.commands:
                execute_command(task)
        else:
            raise UserError(ErrorMessages.invalid_configuration_for_task(self.name))
