# -*- coding: utf-8 -*-
"""PAiP Web Build System - Event Handler Module
This module contains Event Handler Class from Event Sourcing Design Pattern.

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""
# Imports
from pwbs.core.event_sourcing.event import Event
from pwbs.core.event_sourcing.event_bus import EventBus
from pwbs.core.event_sourcing.queue_change_handler import QueueChangeHandler
from pwbs.core.exceptions.event_handle_not_implemented import EventHandleNotImplemented
from abc import ABC
from abc import abstractmethod
from typing import List

# Underscore Variables

"""Author of the module"""
__author__ = 'PAiP Web'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

class EventHandler(QueueChangeHandler, ABC):
    """
    Event Handler Class
    :argument str queue_name: Event Queue Name which this handler is for
    """
    @property
    @abstractmethod
    def queue(self):
        """
        Event Queue Name
        """
        return self.queue

    def __init__(self, queue_name: str):
        super().__init__(queue_name, None)

    def handle(self, current_event: Event, event_queue: List[Event], queue_name: str, event_bus: EventBus):
        try:
            getattr(self, "on_{0}".format(current_event.type))(current_event, event_queue, queue_name, event_bus)
        except AttributeError:
            try:
                getattr(self, "on")(current_event.type, current_event, event_queue, queue_name, event_bus)
            except AttributeError:
                raise EventHandleNotImplemented("Method on_{event_type} and on wasn't implemented")
