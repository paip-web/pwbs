# -*- coding: utf-8 -*-
"""PAiP Web Build System - Simple Event Bus Module
This module contains Simpler Event Bus Class from Event Sourcing Design Pattern.

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""
# Imports
from pwbs.core.event_sourcing.event import Event
from typing import List

# Underscore Variables

"""Author of the module"""
__author__ = 'PAiP Web'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

class EventList:
    """
    :argument List[event] event_store: Event Storage List
    """
    # Event Storage Place
    eventStore: List[Event] = []

    def __init__(self, event_store: List[Event] = None):
        if event_store is not None:
            self.eventStore = event_store

    def get_event_types(self) -> List[str]:
        event_types: List[str] = []
        for event in self.eventStore:
            if event.type not in event_types:
                event_types.append(event.type)
        return event_types

    def __getitem__(self, queried_type: str) -> List[Event]:
        """
        Get Item Magic Method which in this case is for getting list of specified type of events
        :param str queried_type: Type of Event you want to get
        :return List[Event]: List with specified type of events
        """
        events: List[Event] = []
        for event in self.eventStore:
            if event.type is queried_type:
                events.append(event)
        return events

    def __add__(self, other: Event):
        """
        Adds new event to EventBus
        :param event other: Event to add
        :return EventList: This instance with new event
        :raises TypeError: Raised when you trying to add anything else than Event
        """
        if type(other) is Event:
            self.eventStore.append(other)
            return self
        raise TypeError("You can only add Event Class Object to Event Bus")
