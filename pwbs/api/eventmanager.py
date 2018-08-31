# -*- coding: utf-8 -*-
"""PAiP Web Build System - Event Manager

This module is EventManager singleton class for evented programming.

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports

from ..lib.singleton import Singleton, SingletonException

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

    def createEvent(self, name, handlers=None):
        """Create Event"""
        if handlers is None:
            handlers = list()
        self.events[name] = handlers

    def addHandler(self, name, function):
        """Add Handler"""
        self.events[name].append(function)

    def deleteEvent(self, name):
        """Delete Handler"""
        del self.events[name]

    def startEvent(self, event_name, event_name_included=False, **args):
        """Start Event"""
        for f in self.events[event_name]:
            if event_name_included is False:
                f(**args)
            else:
                f(event_name, **args)

    # Event Manager Replacement in Singleton
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if EventManager.__instance is None:
            EventManager()
        return EventManager.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if EventManager.__instance is not None:
            raise SingletonException("This class is a singleton!")
        else:
            EventManager.__instance = self
        self.events = {}
