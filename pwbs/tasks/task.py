# -*- coding: utf-8 -*-
"""PAiP Web Build System - Task Base Class

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from abc import ABC
from abc import abstractmethod
from pwbs.api.task import Task as BaseTask
from pwbs.core import UserError
from pwbs.core.error_messages import ErrorMessages
from pwbs.tasks.task_config import TaskConfig
from pwbs.core.platform import Platform
from pwbs.core.platform import PlatformError

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class Task(BaseTask, ABC):
    """Task Base Class"""

    def __init__(self, config=None):
        """
        Task Initialization Method
        """
        self.config = TaskConfig(config)

    @property
    def comment(self):
        """
        Task Comment
        """
        return self.config.comment

    def process_config(self):
        """
        Process Task Configuration
        """
        if self.config.deprecated:
            raise UserError(ErrorMessages.task_deprecated(self.config.name))
        try:
            Platform.assure_os(self.config.os)
        except PlatformError as e:
            raise UserError(ErrorMessages.task_incorrect_os(self.config.name, e)) from e

    @abstractmethod
    def execute(self, context=None):
        """
        Task Execution Method
        :arg context: Context of Task Execution
        """
        raise NotImplementedError('Not implemented Task Execution Method')

    def __call__(self, context=None):
        """
        Task Execution Method
        :arg context: Context of Task Execution
        """
        self.process_config()
        self.execute(context)
