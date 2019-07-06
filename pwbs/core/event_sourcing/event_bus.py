# -*- coding: utf-8 -*-
"""PAiP Web Build System - Event Bus Module
This module contains Event Bus Class from Event Sourcing Design Pattern.

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""
# Imports
from pwbs.core.event_sourcing.event import Event
from pwbs.core.event_sourcing.queue_change_handler import QueueChangeHandler
from typing import Dict
from typing import List

# Underscore Variables

"""Author of the module"""
__author__ = 'PAiP Web'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

class EventBus(object):
    """
    This is Event Bus Class which is responsible for managing Events in Queues.
    """
    # Event Queues
    queues: Dict[str, List[Event]] = {}
    # Event Queue Handlers
    handlers: Dict[str, List[QueueChangeHandler]] = {}

    def __init__(self):
        self.queues = {}
        self.handlers = {}

    def __getitem__(self, queue_name: str) -> List[Event]:
        """
        Get Queue through get item magic method
        :param str queue_name: Queue Name
        :return List[Event]: List of Events from specified Queue or Empty List otherwise
        """
        try:
            return self.queues[queue_name]
        except KeyError:
            return []

    def emit(self, queue: str, event: Event) -> None:
        """
        Emits a event and adds it to specified queue and executes all handlers in order.
        :param str queue: Queue Name for new Event
        :param Event event: Event to emit to Queue
        """
        if queue not in self.queues.keys():
            self.queues[queue] = []
        self.queues[queue].append(event)
        self._emit_queue_change(queue, event)

    def add_handler(self, event_handler: QueueChangeHandler) -> None:
        """
        Add new Event Queue Handler for specified in handler queue.
        :param QueueChangeHandler event_handler: Event Handler to add to handlers list for specified in handler queue.
        """
        if event_handler.queue not in self.handlers.keys():
            self.handlers[event_handler.queue] = []
        self.handlers[event_handler.queue].append(event_handler)

    def _emit_queue_change(self, queue_name: str, new_event: Event) -> None:
        """
        Emit Queue Change to Event Handlers
        :param str queue_name: Queue Name to Emit Change to
        :param Event new_event: New Event which was added to Events Queue
        """
        for event_handler in self.get_handlers(queue_name):
            event_handler(new_event, self[queue_name], queue_name, self)

    def get_handlers(self, queue_name: str) -> List[QueueChangeHandler]:
        """
        Get All Handlers defined for specified Queue
        :param str queue_name: Queue Name
        :return List[EventHandler]: List of Event Handlers in specified Queue
        """
        try:
            return self.handlers[queue_name]
        except KeyError:
            return []

    def update_handlers(self, queue_name: str, new_handlers: List[QueueChangeHandler]) -> None:
        """
        Update Handlers with completely new object.
        :param str queue_name: Queue Name
        :param List[QueueChangeHandler] new_handlers: New Handlers Object to replace old one
        """
        self.handlers[queue_name] = new_handlers

    def delete_event_from_queue(self, queue: str, event_key: str) -> None:
        """
        Deletes Event with Specified Event Key from Event Queue in Event Bus
        :param str queue: Queue Name
        :param str event_key: UUID of Event to Delete from the queue
        """
        for i, event in enumerate(self.queues[queue]):
            if event.id is event_key:
                del self.queues[queue][i]
