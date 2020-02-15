# -*- coding: utf-8 -*-
"""PAiP Web Build System - Single Task Mode

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT
"""
# Imports
from argparse import Namespace
from typing import List
from typing import Union
from pwbs.tasks.configuration_aware_task import ConfigurationAwareTask
from pwbs.core import service_manager
from pwbs.core import config_manager
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


class SingleTaskMode(ConfigurationAwareTask):
    """Single Command Task Mode Class"""

    @staticmethod
    def init():
        """Initialize Task Mode"""
        task_factory_map[TaskConstants.task_mode().single_task()] = SingleTaskMode
        task_factory_map[TaskConstants.task_mode().multi_command_task()] = SingleTaskMode

    @staticmethod
    def get_forward_arguments(args: Union[None, List[str]]) -> str:
        """
        Get Forward Arguments for Commands in Tasks
        :param args: Forward Arguments
        :return: Suffix for commands in Tasks
        """
        if args is None:
            return ""
        return ' '.join(args)

    @staticmethod
    def preprocess_commands(commands: Union[str, List[str]], arguments: Namespace) -> Union[str, List[str]]:
        """
        Preprocess Commands
        :param commands: Commands for Task
        :param arguments: PWBS Arguments
        :return: Preprocessed Commands for Task
        """
        if isinstance(commands, list):
            new_commands = []
            for cmd in commands:
                new_commands.append(
                    "{0} {1}".format(cmd, SingleTaskMode.get_forward_arguments(arguments.arguments_to_forward))
                )
            return new_commands
        return "{0} {1}".format(commands, SingleTaskMode.get_forward_arguments(arguments.arguments_to_forward))

    @service_manager.inject('log')
    @config_manager.inject('arguments')
    def execute(self, *args, log, arguments, **kwargs):
        """
        Task Execution Method
        """
        commands = SingleTaskMode.preprocess_commands(self.config.commands, arguments)
        # Loop in Commands and their output
        for cmd_in, cmd_out in zip(commands, execute_generator(commands)):
            # Log Execute
            log.log_verbose('Executing "{0}"...'.format(cmd_in), TaskConstants.task_verbose().verbose())
