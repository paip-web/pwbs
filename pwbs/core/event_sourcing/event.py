# -*- coding: utf-8 -*-
"""PAiP Web Build System - Event Class
This module contains Event Class from Event Sourcing Design Pattern.

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""
# Imports
from uuid import uuid4
from typing import Any
from typing import List

# Underscore Variables

"""Author of the module"""
__author__ = 'PAiP Web'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

class Event:
    """
    This is Event Class which is creating events for EventBus.
    :argument str event_type: Type of Event.
    :argument Any event_data: Data for Event.
    """
    # Event Identifier
    id: str = ''
    # Event Type
    type: str = ''
    # Event Data
    data: Any = None

    def __init__(self, event_type: str, event_data: Any):
        self.id = str(uuid4())
        self.type = event_type
        self.data = event_data

    def __delitem__(self, key: List[Any]):
        if (len(key) == 2) or (type(key[0]) is not object) or (type(key[1]) is not str):
            raise TypeError("Not Proper Key to Delete")
        event_bus = key[0]
        event_queue = key[1]
        event_bus.delete_event_from_queue(event_queue, self.id)
