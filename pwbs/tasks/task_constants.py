# -*- coding: utf-8 -*-
"""PAiP Web Build System - Task Constants

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT
"""
# Imports

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class TaskConstants:
    """Task Constants"""

    @staticmethod
    def task_mode():
        """Task Mode Constants"""
        class TaskModeConstants:
            """Task Mode Constants Class"""

            @staticmethod
            def single_task():
                """Single Command Task"""
                return 'sct'

            @staticmethod
            def multi_task():
                """Multi Task Task"""
                return 'mt'

            @staticmethod
            def multi_command_task():
                """Multi Command Task"""
                return 'mc'

            @staticmethod
            def watcher_task():
                """Watcher Task"""
                return 'wt'

            @staticmethod
            def scheduler_task():
                """Scheduler Task"""
                return 'st'

            @staticmethod
            def looper_task():
                """Looper Task"""
                return 'lt'

            @staticmethod
            def argumented_task():
                """Argumented Task"""
                return 'at'

            @staticmethod
            def complex_task():
                """Complex Task"""
                return 'ct'

            @staticmethod
            def plugin_task():
                """Plugin Task"""
                return 'pt'

        return TaskModeConstants

    @staticmethod
    def task_verbose():
        """Task Verbose Constants"""
        class TaskVerboseConstants:
            """Task Verbose Constants Class"""

            @staticmethod
            def none():
                """None - Verbose Level"""
                return 0

            @staticmethod
            def normal():
                """Normal Verbose Level"""
                return 1

            @staticmethod
            def verbose():
                """Verbose -  Verbose Level"""
                return 2

            @staticmethod
            def more_verbose():
                """More Verbose - Verbose Level"""
                return 3

            @staticmethod
            def debug():
                """Debug Verbose Level"""
                return 255

        return TaskVerboseConstants
