# -*- coding: utf-8 -*-
"""PAiP Web Build System - Plugin Base Class

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from abc import ABC
from abc import abstractmethod

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


# Plugin Base Class


class Plugin(ABC):
    """Plugin Base Class"""
    @abstractmethod
    def init(self):
        """
        Plugin Initialization Method
        """
        raise NotImplementedError('Not implemented Plugin Initialization Method')
