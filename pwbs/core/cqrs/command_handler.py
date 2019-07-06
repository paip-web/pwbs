# -*- coding: utf-8 -*-
"""PAiP Web Build System - Command Handler Module
This module contains Command Handler Base Class

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""
# Imports
from pwbs.core.cqrs.command import Command
from pwbs.core.cqrs.command_queue_change_handler import CommandQueueChangeHandler
from pwbs.core.cqrs.command_bus import CommandBus
from pwbs.core.event_sourcing.event_bus import EventBus
from pwbs.core.exceptions.command_handle_not_implemented import CommandHandleNotImplemented
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


class CommandHandler(CommandQueueChangeHandler, ABC):
    """
    Command Handler Class
    :argument str queue_name: Command Queue Name which this handler is for
    """
    @property
    @abstractmethod
    def queue(self):
        """
        Command Queue Name
        """
        return self.queue

    def __init__(self, queue_name: str):
        super().__init__(queue_name, None)

    def handle(self,
               current_event: Command,
               event_queue: List[Command],
               queue_name: str,
               command_bus: CommandBus,
               event_bus: EventBus):
        try:
            getattr(self, "on_{0}".format(current_event.__type__))(
                current_event,
                event_queue,
                queue_name,
                command_bus,
                event_bus)
        except AttributeError:
            try:
                getattr(self, "on")(
                    current_event.__type__,
                    current_event,
                    event_queue,
                    queue_name,
                    command_bus,
                    event_bus)
            except AttributeError:
                raise CommandHandleNotImplemented("Method on_{command_type} and on wasn't implemented")
