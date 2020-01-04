# -*- coding: utf-8 -*-
"""PAiP Web Build System - Single Task Mode

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from pwbs.tasks.task import Task
from pwbs.core import service_manager
from pwbs.tasks.task_factory import task_factory_map
from pwbs.tasks.task_constants import TaskConstants
from pwbs.lib.pwm.pwm_exec import execute_generator

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class SingleTaskMode(Task):
    """Single Command Task Mode Class"""

    @staticmethod
    def init():
        """Initialize Task Mode"""
        task_factory_map[TaskConstants.task_mode().single_task()] = SingleTaskMode
        task_factory_map[TaskConstants.task_mode().multi_command_task()] = SingleTaskMode

    @service_manager.inject('log')
    def execute(self, *args, log, **kwargs):
        """
        Task Execution Method
        """
        log.log_verbose("Running {0} Task...".format(self.name), 1)
        # Loop in Commands and their output
        for cmd_in, cmd_out in zip(self.config.commands, execute_generator(self.config.commands)):
            # Log Execute
            log.log_verbose('Executing "{0}"...'.format(cmd_in), 2)
        # Log Finish
        log.log_verbose("Finished {0} Task...".format(self.name), 1)
