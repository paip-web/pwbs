# -*- coding: utf-8 -*-
"""PAiP Web Build System - Task Constants

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
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
