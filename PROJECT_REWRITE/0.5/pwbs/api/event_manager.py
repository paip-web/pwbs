# -*- coding: utf-8 -*-
"""PAiP Web Build System - Event Manager

This module is Event Manager class for evented programming in PWBS.
This class if for elements which will need Event Manager but not need to hook into PWBS Events.

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Event Manager Class


class EventManager(object):
    """Event Manager Class"""

    def __init__(self):
        """Event Manager Constructor"""
        self.events = {}

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

    def startEvent(self, event_name, event_name_included=True, **args):
        """Start Event"""
        for f in self.events[event_name]:
            if event_name_included is False:
                f(**args)
            else:
                f(event_name, **args)
