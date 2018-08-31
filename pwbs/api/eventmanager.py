# -*- coding: utf-8 -*-
"""PAiP Web Build System - Event Manager

This module is EventManager singleton class for evented programming.

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports

from ..lib.singleton import Singleton

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Event Manager Class

class EventManager(Singleton):
    """Event Manager Class"""

    def __init__(self):
        super().__init__()
        self.__events = {}

    def createEvent(self, name, handlers=None):
        """Create Event"""
        if handlers is None:
            handlers = list()
        self.__events[name] = handlers

    def addHandler(self, name, function):
        """Add Handler"""
        self.__events[name].append(function)

    def deleteEvent(self, name):
        """Delete Handler"""
        del self.__events[name]

    def startEvent(self, name, **args):
        """Start Event"""
        for f in self.__events[name]:
            f(**args)
