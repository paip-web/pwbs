# -*- coding: utf-8 -*-
"""PAiP Web Build System - Plugin Event Manager

This module is Plugin Event Manager class for evented programming in PWBS.
This class if for plugins events because it need own system as well as PWBS Event Manager.

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports

from .event_manager import EventManager

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Event Manager Class


class PluginEventManager(EventManager):
    """Plugin Event Manager Class"""
    @staticmethod
    def initialize():
        PEM = PluginEventManager()
        # PWBS Event Called on Initializing Plugin | This need to be called in PWBS itself
        PEM.createEvent("pwbs-event--plugin-initialize")
        # PWBS Event Called on main function start
        PEM.createEvent("pwbs-event--plugin-main-start")
        # PWBS Event Called on main function end
        PEM.createEvent("pwbs-event--plugin-main-end")
        # PWBS Event Called on delete of instance
        PEM.createEvent("pwbs-event--plugin-uninitialize")
        return PEM
