# -*- coding: utf-8 -*-
"""PAiP Web Build System - Task Interpreter Plugin

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from pwbs.api.plugin import Plugin
from pwbs.core import service_manager
from pwbs.core import event_manager
from pwbs.core import config_manager as configuration

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class TaskPlugin(Plugin):
    """Initialization Plugin Class"""

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
    @configuration.inject('commands')
    def run_task(*args, nf, commands, task, **kwargs):
        commands[task].run()
        return nf(*args, **kwargs)
