# -*- coding: utf-8 -*-
"""PAiP Web Build System - API Helpers Module

This module is helper functions to operate with public api of PWBS easier.

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from pwbs.core.pipeline import forwarder_stage

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# On Task Plugin Helper


def on_task(task_name: str):
    """
    Call this plugin on specified task name
    :param task_name: Task Name
    """

    def inject(injection_destination):
        """
        Injector Decorator
        :param injection_destination: Decorated Place
        """
        def injector(*args, task, **kwargs):
            """Injector"""
            if task == task_name:
                return injection_destination(*args, task=task, **kwargs)
            return forwarder_stage(*args, task=task, **kwargs)
        return injector
    return inject
