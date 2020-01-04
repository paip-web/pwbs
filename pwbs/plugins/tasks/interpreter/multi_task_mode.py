# -*- coding: utf-8 -*-
"""PAiP Web Build System - MultiTask Mode

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from pwbs.tasks.task import Task
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


class MultiTaskMode(Task):
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
        log.log_verbose("Running {0} Task...".format(self.name), 1)
        # Loop in Commands and their output
        for task in self.config.extends.split(','):
            # Log Execute
            log.log_verbose('Executing "{0}"...'.format(task), 2)
            if task not in tasks:
                raise UserError(ErrorMessages.task_not_found(task))
            tasks[task](*args, tasks=tasks, **kwargs)
        # Log Finish
        log.log_verbose("Finished {0} Task...".format(self.name), 1)
