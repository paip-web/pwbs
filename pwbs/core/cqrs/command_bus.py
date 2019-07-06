# -*- coding: utf-8 -*-
"""PAiP Web Build System - Command Bus Module
This module contains Command Bus Class

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""
# Imports
from pwbs.core.cqrs.command import Command
from pwbs.core.cqrs.command_handler import CommandHandler
from pwbs.core.common.bus import Bus
from pwbs.core.exceptions.command_handle_error import CommandHandleError
from typing import Dict

# Underscore Variables
"""Author of the module"""
__author__ = 'PAiP Web'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class CommandBus(Bus[Command, CommandHandler]):
    handlers: Dict[str, CommandHandler] = {}

    def add_handler(self, command_handler: CommandHandler) -> None:
        if command_handler in self.handlers.values():
            raise CommandHandleError("Command Handler already used in this Command Bus")
        self.handlers[command_handler.queue] = command_handler

    def _emit_queue_change(self, queue_name: str, new_event: Command) -> None:
        """
        Emit Queue Change to Command Handler
        :param str queue_name: Queue Name to Emit Change to
        :param Event new_event: New Element which was added to Elements Queue
        """
        event_handler = self.get_handlers(queue_name)
        event_handler(new_event, self[queue_name], queue_name, self)
        self.delete_event_from_queue(queue_name, new_event.__type__)

    def update_handlers(self, queue_name: str, new_handler: CommandHandler) -> None:
        """
        Update Handler with completely new one.
        :param str queue_name: Queue Name
        :param CommandHandler new_handler: New Handlers Object to replace old one
        """
        self.handlers[queue_name] = new_handler

    def delete_event_from_queue(self, queue: str, command_type: str) -> None:
        """
        Deletes Command with Specified Command Type from Command Queue in Bus
        :param str queue: Queue Name
        :param str command_type: Type of Command to Delete from the queue
        """
        for i, command in enumerate(self.queues[queue]):
            if command.__type__ is command_type:
                del self.queues[queue][i]
