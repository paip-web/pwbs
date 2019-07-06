# -*- coding: utf-8 -*-
"""PAiP Web Build System - Command Handle Not Implemented Exception Module
This module contains Command Handle Not Implemented Exception for raising custom Exception.
It's raised when CommandHandler SubClass doesn't implement on or on_{command_type} methods.

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""

# Underscore Variables

"""Author of the module"""
__author__ = 'PAiP Web'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

class CommandHandleNotImplemented(NotImplementedError):
    """
    Exception raised when EventHandler SubClass doesn't implement on or on_{event_type} methods.
    """
    pass
