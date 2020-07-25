# -*- coding: utf-8 -*-
"""PAiP Web Build System - Example Plugin

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT
"""
# Imports
from pwbs.api.plugin import Plugin

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class ExamplePlugin(Plugin):
    """Example Plugin Class"""

    def __init__(self):
        self.test = 21

    def init(self):
        """
        Plugin Initialization Method
        """
        self.test = 22
        print('Example Plugin Initialized')
