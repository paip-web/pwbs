# -*- coding: utf-8 -*-
"""PAiP Web Build System - Task Mode Plugin

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from pwbs.api.plugin import Plugin
from pwbs.plugins.tasks.interpreter.single_task_mode import SingleTaskMode
from pwbs.plugins.tasks.interpreter.multi_task_mode import MultiTaskMode

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class TaskModePlugin(Plugin):
    """Initialization Plugin Class"""

    def init(self):
        """
        Plugin Initialization Method
        """
        SingleTaskMode.init()
        MultiTaskMode.init()
