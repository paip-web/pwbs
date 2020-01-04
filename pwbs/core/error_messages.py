# -*- coding: utf-8 -*-
"""PAiP Web Build System - Error Messages

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from pwbs.core.platform import PlatformError

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class ErrorMessages:
    """Task Constants"""

    @staticmethod
    def task_deprecated(name: str) -> str:
        """
        Deprecated Task Error
        :param str name: Name of Task
        :return str: Error Message
        """
        return "Task {0} is marked as deprecated".format(name)

    @staticmethod
    def task_incorrect_os(task_name: str, platform_error: PlatformError) -> str:
        """
        Task Incorrect Operating System Error
        :param str task_name: Name of Task
        :param PlatformError platform_error: Platform Error
        :return str: Error Message
        """
        return "Task {0} is incompatible with your system, {1}".format(task_name, str(platform_error))

    @staticmethod
    def incorrect_os(actual_os: str, os: str) -> str:
        """
        Incorrect Operating System Error
        :param actual_os: Actual OS
        :param os: Asserted OS
        :return str: Error Message
        """
        return "Your os is {0} not {1}".format(actual_os, os)
