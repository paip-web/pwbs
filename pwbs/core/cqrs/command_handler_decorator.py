# -*- coding: utf-8 -*-
"""PAiP Web Build System - Command Handler Decorator Module
This module contains Command Handler Decorator,
that makes Command handlers from functions.

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""
# Imports
from typing import List, Any
from pwbs.core.cqrs.command import Command
from pwbs.core.cqrs.command_handler import CommandHandler
from pwbs.core.cqrs.command_bus import CommandBus
from pwbs.core.event_sourcing.event_bus import EventBus

# Underscore Variables
"""Author of the module"""
__author__ = 'PAiP Web'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


def command_handler_decorator(handler_function):
    """
    Decorator for making Command Handler from functions
    :param handler_function:
    :return: Generated command handler
    :rtype: CommandHandler
    """
    def wrapper(queue_name, event_name) -> CommandHandler:
        class GeneratedCommandHandler(CommandHandler):
            """
            Generated Command Handler for decorated function
            """
            def on(self,
                   event_type: Any,
                   current_event: Command,
                   event_queue: List[Command],
                   on_queue_name: str,
                   command_bus: CommandBus,
                   event_bus: EventBus):
                """
                Events Handler
                :param event_type: Event Type Name
                :param current_event: Current Event
                :param event_queue: Current Event Queue
                :param on_queue_name: Queue Name
                :param command_bus: Command Bus
                :param event_bus: Event Bus
                :return: Nothing
                :rtype: None
                :raises AttributeError: On not handled event type
                """
                if event_type is event_name:
                    handler_function(
                        current_event=current_event,
                        event_queue=event_queue,
                        queue_name=on_queue_name,
                        command_bus=command_bus,
                        event_bus=event_bus,
                        event_type=event_type,
                    )
                else:
                    raise AttributeError('Not supported event')
        return GeneratedCommandHandler(queue_name)
    return wrapper
