# -*- coding: utf-8 -*-
"""PAiP Web Build System - Task Interpreter Plugin

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from pwbs.api.plugin import Plugin
from pwbs.core import event_manager
from pwbs.core import config_manager as configuration
from pwbs.core import UserError
from pwbs.core.error_messages import ErrorMessages

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class TaskPlugin(Plugin):
    """Task Interpreter Plugin Class"""

    def init(self):
        """
        Plugin Initialization Method
        """
        pass

    @staticmethod
    @event_manager.handler_decorator('@pwbs/interpreter/task')
    @configuration.inject('arguments')
    def main(*args, nf, arguments, **kwargs):
        """Task Interpreter"""
        for arg in arguments.Task:
            event_manager('@pwbs/interpreter/interpret_task', task=arg)
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/interpreter/interpret_task')
    @configuration.inject('tasks')
    def run_task(*args, nf, tasks, task, **kwargs):
        """Run Task"""
        if task in tasks:
            tasks[task](*args, **kwargs, tasks=tasks, task=task)
            return True
        return nf(*args, task=task, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@after_@pwbs/interpreter/interpret_task')
    def error_if_not_found(*args, nf, **kwargs):
        """Error if no task was called"""
        if 'task' in kwargs.keys():
            raise UserError(ErrorMessages.task_not_found(kwargs['task']))
        raise UserError(ErrorMessages.no_task_called())
