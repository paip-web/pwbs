# -*- coding: utf-8 -*-
"""PAiP Web Build System - Main Plugin

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from pwbs.api.plugin import Plugin
from pwbs.core import event_manager
from pwbs.core import NotImplementedFeatureError

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class MainPlugin(Plugin):
    """Main Plugin Class"""

    def init(self):
        """
        Plugin Initialization Method
        """
        pass

    @staticmethod
    @event_manager.handler_decorator('@pwbs/main')
    def main(*args, nf, **kwargs) -> None:
        """Main Function of PWBS"""
        try:
            event_manager('@pwbs/init', *args, **kwargs)
            event_manager('@pwbs/main/main', *args, **kwargs)
        except NotImplementedFeatureError as e:
            print("Not Implemented Feature Called!")
            print(e)
        except SystemExit as e:
            event_manager('@pwbs/main/catch/SystemExit', exception=e, *args, **kwargs)
        except KeyboardInterrupt as e:
            event_manager('@pwbs/main/catch/KeyboardInterrupt', exception=e, *args, **kwargs)
        except BaseException as e:
            event_manager('@pwbs/main/catch', exception=e, *args, **kwargs)
            raise e
        finally:
            event_manager('@pwbs/main/finally', *args, **kwargs)
            event_manager('@pwbs/main/unload', *args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/main/main')
    def main_pwbs(*args, nf, **kwargs):
        """Main Function"""
        special_task_executed = event_manager('@pwbs/interpreter/special', *args, **kwargs)
        if special_task_executed:
            return None
        event_manager('@pwbs/interpreter/task', *args, **kwargs)
        return nf(*args, **kwargs)
