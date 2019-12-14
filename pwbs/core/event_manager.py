# -*- coding: utf-8 -*-
"""PAiP Web Build System - Event Manager

This module is Event Manager class for managing events in PWBS.

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from typing import NewType
from typing import List
from typing import Dict
from typing import Any
from typing import Union
from pwbs.core.pipeline import Pipeline

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Event Manager Class

EventName = NewType('EventName', str)
EventType = NewType('EventType', Any)


class EventManager:
    """Event Manager Class"""

    """Events registered in Event Manager"""
    events: Dict[EventName, List[EventType]] = {}

    def __init__(self):
        """Event Manager Constructor"""
        self.events = {}

    def __setitem__(self, event_name: EventName, event_handler: EventType) -> None:
        """Event Manager Registration"""
        if event_name not in self.events.keys():
            self.events[event_name] = []
        self.events[event_name].append(event_handler)

    def __getitem__(self, event_name: EventName) -> Union[EventType, None]:
        """Event Manager Get Event Method"""
        if event_name in self.events.keys():
            return self.events[event_name]
        return None

    def __delitem__(self, event_name: EventName) -> None:
        """Pipeline Delete Stage Method"""
        del self.events[event_name]

    def __contains__(self, check: Union[EventName, EventType]) -> bool:
        """Pipeline Is in Method2"""
        if isinstance(check, str):
            return check in self.events.keys()
        ret = False
        for ev_handlers in self.events.values():
            if ret:
                break
            for ev_handler in ev_handlers:
                if ret:
                    break
                if check is ev_handler:
                    ret = True
        return ret

    @staticmethod
    def merge_events(*event_handlers_lists: List[EventType]):
        """
        Merge Event Lists
        :param event_handlers_lists: Event Handlers Lists
        :return: Merged Event Handler List
        """
        result = []
        for event_handlers_list in event_handlers_lists:
            if event_handlers_list is not None:
                result.extend(event_handlers_list)
        return result

    def get_event(self, event_name: EventName) -> List[EventType]:
        """
        Get Event handlers with before, after and global event handlers
        :param event_name: Event Name to get handlers for
        :return: Event Handlers
        """
        return EventManager.merge_events(
            self['@before_*'],
            self["@before_{}".format(event_name)],
            self[event_name],
            self['*'],
            self["@after_{}".format(event_name)],
            self['@after_*'],
        )

    def __call__(self, event_name: EventName, *args, **kwargs) -> Any:
        """
        Execute Event
        :param event_name: Event to Execute
        """
        return Pipeline.from_list(self.get_event(event_name))(*args, **kwargs)

    def handler_decorator(self, event_name: EventName):
        """
        Event Handler Decorator
        :param event_name: Event Name
        """

        def inject(injection_destination):
            """
            Injector Decorator
            :param injection_destination: Decorated Place
            """
            if injection_destination not in self:
                self[event_name] = injection_destination

            def injector(*args, **kwargs):
                """Injector"""
                return injection_destination(*args, **kwargs)

            return injector

        return inject
