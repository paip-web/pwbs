# -*- coding: utf-8 -*-
"""PAiP Web Build System - Plugin

This module is Plugin class for future plugin development for PWBS.

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports

import abc
from .pwbs_event_manager import PWBSEventManager
from .plugin_event_manager import PluginEventManager

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Plugin Class

class BasePlugin(object):
    """Base Plugin Class"""
    # Abstract Class Metaclass
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor of BasePlugin Class"""
        # PWBS Event Manager
        self._pwbsem = PWBSEventManager.getInstance()
        # PWBS Plugin Event Manager
        self.event_manager = PluginEventManager.initialize()


    def __call__(self, **kwargs):
        """Call magic method of BasePlugin Class
        It's called upon initilization of Plugin.
        """
        self.event_manager.startEvent("pwbs-event--plugin-main-start", args=kwargs, this=self)
        self.main()
        self.event_manager.startEvent("pwbs-event--plugin-main-end", args=kwargs, this=self)

    def __del__(self):
        """Destructor"""
        self.event_manager.startEvent("pwbs-event--plugin-uninitialize", this=self)

    @abc.abstractmethod
    def main(self):
        """Main Plugin Function
        It need to be implemented in Plugin
        """
        pass
