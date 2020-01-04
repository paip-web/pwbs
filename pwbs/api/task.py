# -*- coding: utf-8 -*-
"""PAiP Web Build System - Task Base Class

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


# Task Base Class


class Task(ABC):
    """Task Base Class"""
    @abstractmethod
    def __init__(self):
        """
        Task Initialization Method
        """
        raise NotImplementedError('Not implemented Task Initialization Method')

    @abstractmethod
    @property
    def comment(self):
        """Comment of the task"""
        return ''

    @abstractmethod
    def __call__(self, context=None):
        """
        Task Execution Method
        :arg context: Context of Task Execution
        """
        raise NotImplementedError('Not implemented Task Execution Method')
