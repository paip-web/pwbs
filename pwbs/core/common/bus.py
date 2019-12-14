# -*- coding: utf-8 -*-
"""PAiP Web Build System - Bus Module
This module contains Bus Class.

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""
# Imports
from typing import Dict
from typing import List
from typing import Generic
from typing import TypeVar

# Underscore Variables

"""Author of the module"""
__author__ = 'PAiP Web'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

BusType = TypeVar("BusType")
HandlerType = TypeVar("HandlerType")


class Bus(Generic[BusType, HandlerType]):
    """
    This is Bus Class which is responsible for managing Elements in Queues.
    """
    # Event Queues
    queues: Dict[str, List[BusType]] = {}
    # Event Queue Handlers
    handlers: Dict[str, List[HandlerType]] = {}

    def __init__(self):
        self.queues = {}
        self.handlers = {}

    def __getitem__(self, queue_name: str) -> List[BusType]:
        """
        Get Queue through get item magic method
        :param str queue_name: Queue Name
        :return List[BusType]: List of Elements from specified Queue or Empty List otherwise
        """
        try:
            return self.queues[queue_name]
        except KeyError:
            return []

    def emit(self, queue: str, event: BusType) -> None:
        """
        Emits a element and adds it to specified queue and executes all handlers in order.
        :param str queue: Queue Name for new Element
        :param Event event: Event to emit to Queue
        """
        if queue not in self.queues.keys():
            self.queues[queue] = []
        self.queues[queue].append(event)
        self._emit_queue_change(queue, event)

    def add_handler(self, event_handler: HandlerType) -> None:
        """
        Add new Element Queue Handler for specified in handler queue.
        :param HandlerType event_handler: Element Handler to add to handlers list for specified in handler queue.
        """
        if event_handler.queue not in self.handlers.keys():
            self.handlers[event_handler.queue] = []
        self.handlers[event_handler.queue].append(event_handler)

    def _emit_queue_change(self, queue_name: str, new_event: BusType) -> None:
        """
        Emit Queue Change to Element Handlers
        :param str queue_name: Queue Name to Emit Change to
        :param Event new_event: New Element which was added to Elements Queue
        """
        for event_handler in self.get_handlers(queue_name):
            event_handler(new_event, self[queue_name], queue_name, self)

    def get_handlers(self, queue_name: str) -> List[HandlerType]:
        """
        Get All Handlers defined for specified Queue
        :param str queue_name: Queue Name
        :return List[HandlerType]: List of Element Handlers in specified Queue
        """
        try:
            return self.handlers[queue_name]
        except KeyError:
            return []

    def update_handlers(self, queue_name: str, new_handlers: List[HandlerType]) -> None:
        """
        Update Handlers with completely new object.
        :param str queue_name: Queue Name
        :param List[HandlerType] new_handlers: New Handlers Object to replace old one
        """
        self.handlers[queue_name] = new_handlers

    def delete_event_from_queue(self, queue: str, event_key: str) -> None:
        """
        Deletes Element with Specified Element Key from Element Queue in Bus
        :param str queue: Queue Name
        :param str event_key: UUID of Element to Delete from the queue
        """
        for i, event in enumerate(self.queues[queue]):
            if event.id is event_key:
                del self.queues[queue][i]
