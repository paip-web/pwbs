# -*- coding: utf-8 -*-
"""PAiP Web Build System - Core Module
This module contains the most core functionality,
needed by other functions and classes.

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from datetime import datetime
from pwbs.core.event_manager import EventManager
from pwbs.core.service_manager import ServiceManager
from pwbs.core.plugin_manager import PluginManager

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Globals for PWBS
service_manager = ServiceManager()
event_manager = EventManager()
"""Initialization of Service Manager"""
service_manager['plugin_manager'] = PluginManager()
service_manager['event_manager'] = event_manager
service_manager['service_manager'] = service_manager


def prefix_text(text=""):
    """Function to prefix text
    Default Prefixer
    Args:
        text (:obj:`str`): Text to prefix
    """
    return "PWBS[{0}]: {1}".format(datetime.now().strftime("%H:%M:%S"), text)


class NotImplementedFeatureError(NotImplementedError):
    """Error for Not Implemented Functionality"""
    pass
