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
from pwbs.core.common.bus import Bus

# Underscore Variables

"""Author of the module"""
__author__ = 'PAiP Web'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

class EventBus(Bus[Event, QueueChangeHandler]):
    pass
