# -*- coding: utf-8 -*-
"""PAiP Web Build System - Data Model Module
This module contains Data Model Class.

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""
# Imports
from pwbs.core.event_sourcing.event_handler import EventHandler
from pwbs.core.event_sourcing.event import Event
from pwbs.core.event_sourcing.event_bus import EventBus
from typing import List
from typing import Dict
from typing import Any

# Underscore Variables

"""Author of the module"""
__author__ = 'PAiP Web'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

class DataModelHandler(EventHandler):
    queue = 'DataModel'
    data_model: Any = None

    def __init__(self, data_model: Any):
        super().__init__(self.queue)
        self.data_model = data_model

    def on_update(self, current_event: Event, event_queue: List[Event], queue_name: str, event_bus: EventBus):
        self.data_model.update_data(current_event.data)
        del current_event[[event_bus, queue_name]]

class DataModel:
    data: Dict[Any, Any] = {}

    def update_data(self, newData: Dict[Any, Any]):
        self.data = {**self.data, **newData}

    def get_handler(self):
        return DataModelHandler(self)

    def get_data(self):
        return self.data
