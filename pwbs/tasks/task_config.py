# -*- coding: utf-8 -*-
"""PAiP Web Build System - Task Config Class

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from typing import Dict
from sentry_sdk.scope import Scope
from pwbs.tasks.task_constants import TaskConstants as Constants
from pwbs.core.platform import Platform

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class TaskConfig:
    """Task Config Class"""

    def __init__(self, config: Dict = None):
        """
        Task Initialization Method
        """
        if config is None:
            config = {}

        """Name of Task"""
        self.name = config.get('name', '')

        """Comment of Task"""
        self.comment = config.get('comment', '')

        """Mode of Task"""
        self.mode = config.get('mode', Constants.task_mode().single_task())

        """Commands"""
        self.commands = config.get('commands', [])

        """Arguments of Task"""
        self.arguments = config.get('arguments', [])

        """Is task meant to run asynchronous"""
        self.asynchronous = config.get('async', False)

        """Task Configuration"""
        self.configuration = config.get('configuration', {})

        """Tasks that this derives from"""
        self.extends = config.get('extends', '')

        """Verbose Level of this task"""
        self.verbose = config.get('verbose', None)

        """Debug Mode of this task"""
        self.debug = config.get('debug', None)

        """Is task meant to be run through docker"""
        self.docker = config.get('dockerized', False)

        """OS that this task need to work on"""
        self.os = Platform.get_os_from_alias(config.get('os', Platform.os().any()))

        """Is task deprecated"""
        self.deprecated = config.get('deprecated', False)

        """Configuration Data"""
        self.data = config

    def attach_to_sentry(self, scope: Scope):
        """Attach configuration information to sentry scope"""
        scope.set_extra("task_name", self.name)
        scope.set_extra("task_commands", self.commands)
        scope.set_extra("task_comment", self.comment)
        scope.set_extra("task_mode", self.mode)
        scope.set_extra("task_arguments", self.arguments)
        scope.set_extra("task_async", self.asynchronous)
        scope.set_extra("task_configuration", self.configuration)
        scope.set_extra("task_extends", self.extends)
        scope.set_extra("task_verbose", self.verbose)
        scope.set_extra("task_debug", self.debug)
        scope.set_extra("task_docker", self.docker)
        scope.set_extra("task_deprecated", self.deprecated)
        scope.set_extra("task_data", self.data)
