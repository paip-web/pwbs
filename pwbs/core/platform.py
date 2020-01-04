# -*- coding: utf-8 -*-
"""PAiP Web Build System - Platform Class

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
import platform
from pwbs.core.error_messages import ErrorMessages
from pwbs.core import PlatformError

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class Platform:
    """Platform Class"""

    @staticmethod
    def os():
        """
        Operating System Constants
        """
        class OSConstants:
            """OS Constants Class"""

            @staticmethod
            def windows() -> str:
                """Windows OS"""
                return 'windows'

            @staticmethod
            def linux() -> str:
                """Linux OS"""
                return 'linux'

            @staticmethod
            def mac() -> str:
                """Mac OS"""
                return 'mac'

            @staticmethod
            def other() -> str:
                """Other OS"""
                return 'other'

            @staticmethod
            def any() -> str:
                """Any OS"""
                return 'any'

            @staticmethod
            def all():
                """All OS"""
                return (
                    OSConstants.linux(),
                    OSConstants.windows(),
                    OSConstants.mac(),
                    OSConstants.other(),
                    OSConstants.any()
                )

        return OSConstants

    @staticmethod
    def get_os_from_alias(alias: str) -> str:
        """
        Get OS from its alias
        :param str alias: Alias
        :return str: Operating System Constant
        """
        alias = alias.lower()
        if alias in Platform.os().all():
            return alias
        if alias in ['win', 'w', 'windows']:
            return Platform.os().windows()
        if alias in ['linux', 'lin']:
            return Platform.os().linux()
        if alias in ['mac os x', 'osx']:
            return Platform.os().mac()
        return Platform.os().other()

    @staticmethod
    def assure_os(os: str) -> None:
        """
        Assure that you are on correct operating system
        :param os: System that you want to enforce
        """
        real_os = Platform.get_os_from_alias(os)
        if real_os == Platform.os().any():
            return
        actual_os = Platform.get_os()
        if actual_os == real_os:
            return
        raise PlatformError(ErrorMessages.incorrect_os(actual_os, real_os))

    @staticmethod
    def get_os() -> str:
        """
        Get Actual Operating System
        :return: Current Operating System
        """
        actual_os = platform.system()
        if actual_os == 'Windows':
            return Platform.os().windows()
        if actual_os == 'Linux':
            return Platform.os().linux()
        if actual_os == 'Mac OS X':
            return Platform.os().mac()
        return Platform.os().other()
