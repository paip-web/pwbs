# -*- coding: utf-8 -*-
"""PAiP Web Build System - Runner Base Class

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


# Runner Base Class


class Runner(ABC):
    """Runner Base Class"""
    def __init__(self):
        """
        Runner Constructor
        """
        self.return_code = None

        self.init()

    @abstractmethod
    def init(self):
        """
        Runner Initialization Method
        """
        raise NotImplementedError('Not implemented Runner Initialization Method')

    @abstractmethod
    def execute(self, command: str, *args, **kwargs):
        """
        Runner Execution Method
        """
        raise NotImplementedError('Not implemented Runner Initialization Method')
