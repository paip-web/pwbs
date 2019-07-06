# -*- coding: utf-8 -*-
"""PAiP Web Build System - Command Handle Error Exception Module
This module contains Command Handle Error Exception for raising custom Exception.

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

class CommandHandleError(TypeError):
    """
    Exception raised when CommandHandler already exists in CommandBus
    """
    pass
