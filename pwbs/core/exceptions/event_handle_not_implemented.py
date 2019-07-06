# -*- coding: utf-8 -*-
"""PAiP Web Build System - Event Handle Not Implemented Exception Module
This module contains Event Handle Not Implemented Exception for raising custom Exception.
It's raised when EventHandler SubClass doesn't implement on or on_{event_type} methods.

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

class EventHandleNotImplemented(NotImplementedError):
    """
    Exception raised when EventHandler SubClass doesn't implement on or on_{event_type} methods.
    """
    pass
