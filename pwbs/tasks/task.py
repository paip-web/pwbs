# -*- coding: utf-8 -*-
"""PAiP Web Build System - Task Base Class

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT
"""
# Imports
from abc import ABC
from abc import abstractmethod
import sentry_sdk
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
        if isinstance(config, TaskConfig):
            self.config = config
        else:
            self.config = TaskConfig(config)

    @property
    def name(self):
        """
        Task Name
        """
        return self.config.name

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
            raise UserError(ErrorMessages.task_deprecated(self.name))
        try:
            Platform.assure_os(self.config.os)
        except PlatformError as e:
            raise UserError(ErrorMessages.task_incorrect_os(self.name, e)) from e

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Task Execution Method
        """
        raise NotImplementedError('Not implemented Task Execution Method')

    def __call__(self, *args, **kwargs):
        """
        Task Execution Method
        """
        self.process_config()
        with sentry_sdk.configure_scope() as scope:
            self.config.attach_to_sentry(scope)
        self.execute(*args, **kwargs)
