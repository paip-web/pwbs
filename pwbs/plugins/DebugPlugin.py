# -*- coding: utf-8 -*-
"""PAiP Web Build System - Debug Plugin

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from datetime import datetime
from pwbs.api.plugin import Plugin
from pwbs.core import event_manager
from pwbs.core import service_manager
from pwbs.core import config_manager

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

debug = False


class DebugPlugin(Plugin):
    """Debug Plugin Class"""

    def init(self):
        """
        Plugin Initialization Method
        """
        if debug:
            DebugPlugin.log('Debug Plugin is loaded')

    @staticmethod
    def log(text=""):
        """Logger"""
        print("PWBS-DEBUG[{0}]: {1}".format(datetime.now().strftime("%H:%M:%S"), text))

    @staticmethod
    @event_manager.handler_decorator('@before_*')
    def main_before(*args, nf, **kwargs):
        """Debugger Plugin"""
        if debug:
            DebugPlugin.log('BEFORE: {} | DATA: arg: {} kwargs: {}'.format(kwargs['@event'], args, kwargs))
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('*')
    def main(*args, nf, **kwargs):
        """Debugger Plugin"""
        if debug:
            DebugPlugin.log('GLOBAL: {} | DATA: arg: {} kwargs: {}'.format(kwargs['@event'], args, kwargs))
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@after_*')
    def main_after(*args, nf, **kwargs):
        """Debugger Plugin"""
        if debug:
            DebugPlugin.log('AFTER: {} | DATA: arg: {} kwargs: {}'.format(kwargs['@event'], args, kwargs))
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@after_@pwbs/main/catch')
    def main_catcher(*args, nf, exception=None, **kwargs):
        """Debugger Plugin"""
        if debug:
            DebugPlugin.log('CATCHER: {}'.format(exception))
            raise exception
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@after_@pwbs/main/unload')
    def unloader(*args, nf, **kwargs):
        """Debugger Plugin"""
        if debug:
            DebugPlugin.log('Services: {} | Config: {}'.format(service_manager.services, config_manager.config))
            if 'config_manager' in service_manager:
                print(service_manager['config_manager'].configmanager.config_filename)
        return nf(*args, **kwargs)
