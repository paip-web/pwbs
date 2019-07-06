# -*- coding: utf-8 -*-
"""PAiP Web Build System - Command Module
This module contains Command Base Class

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""
# Imports
from abc import ABC
from abc import abstractmethod

# Underscore Variables
"""Author of the module"""
__author__ = 'PAiP Web'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class Command(ABC):
    """
    Command Base Class
    """
    @property
    @abstractmethod
    def __type__(self):
        """
        Type of Command
        """
        return self.__type__

    def __call__(self):
        """
        Get Data from Command
        """
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        members_values = [getattr(self, member) for member in members]
        return dict(zip(members, members_values))
