# -*- coding: utf-8 -*-
"""PAiP Web Build System - CQRS Module
This module contains Commands and Queries from cqrs design

NAME - PAiP Web Build System
AUTHOR - PAiP Web <paipweb@paipweb.com>
LICENSE - MIT

"""
# Imports
from pwbs.core.cqrs.command import Command
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

CommandHandleType = Callable[[Command, List[Command], str, Any, Command], None]

class CommandQueueChangeHandler:
    """
    Command Queue Change Handler Class
    :argument str queue_name: Queue Name
    :argument Optional[CommandHandleType] handler_function: Command Queue Change Handler Function
    """
    # Event Queue Name
    queue: str = ''
    # Handle of Event
    handle: CommandHandleType = lambda: None

    def __init__(self, queue_name: str, handler_function: Optional[CommandHandleType, None]):
        self.queue = queue_name
        if handler_function is not None:
            self.handle = handler_function

    def __call__(self, current_command: Command, command_queue: List[Command], queue_name: str, command_bus: Any, event_bus: Any):
        """
        Call Magic method which calls to run queue change event handler
        :param Event current_command: Current Command to Handle
        :param List[Command] command_queue: Command Queue
        :param str queue_name: Command Queue Name
        :param CommandBus command_bus: Command Bus Instance
        :param EventBus event_bus: Event Bus Instance
        """
        self.handle(current_command, command_queue, queue_name, command_bus, event_bus)
