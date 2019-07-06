# -*- coding: utf-8 -*-
"""PAiP Web Build System - Event Handler Module
This module contains Event Handler Class from Event Sourcing Design Pattern.

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""
# Imports
from pwbs.core.event_sourcing.event import Event
from typing import List
from typing import Callable
from typing import Any
from typing import Optional

# Underscore Variables

"""Author of the module"""
__author__ = 'PAiP Web'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

class QueueChangeHandler:
    """
    Queue Change Handler Class
    :argument str queue_name: Queue Name
    :argument Callable[[Event, List[Event], str, Any], None] handler_function: Queue Change Handler Function
    """
    # Event Queue Name
    queue: str = ''
    # Handle of Event
    handle: Callable[[Event, List[Event], str, Any], None] = lambda: None

    def __init__(self, queue_name: str, handler_function: Optional[Callable[[Event, List[Event], str, Any], None]]):
        self.queue = queue_name
        if handler_function is not None:
            self.handle = handler_function

    def __call__(self, current_event: Event, event_queue: List[Event], queue_name: str, event_bus: Any):
        """
        Call Magic method which calls to run queue change event handler
        :param Event current_event: Current Event to Handle
        :param List[Event] event_queue: Event Queue
        :param str queue_name: Event Queue Name
        :param EventBus event_bus: Event Bus Instance
        """
        self.handle(current_event, event_queue, queue_name, event_bus)
