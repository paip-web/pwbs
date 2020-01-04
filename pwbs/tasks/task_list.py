# -*- coding: utf-8 -*-
"""PAiP Web Build System - Task List Class

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from typing import List
from pwbs.api.task import Task

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class TaskList:
    """Task List Class"""

    def __init__(self, value: List[Task]):
        """Constructor of the Class"""
        self.tasks = value

    def __getitem__(self, key):
        """Dictionary Based Getting Value Overload Function"""
        for task in self.tasks:
            if key in (task, task.name):
                return task
        raise KeyError("Key {} not found!".format(key))

    def __setitem__(self, key, value):
        """Dictionary Based Setting Value Overload Function"""
        old_tasks = self.tasks
        self.tasks = []
        # New Item Fallback
        item_set = False
        # Loop
        for task in old_tasks:
            if key in (task, task.name):
                item_set = True
                self.tasks.append(value)
            else:
                self.tasks.append(task)
        if item_set is False:
            self.tasks.append(value)

    def __delitem__(self, key):
        """Dictionary Based Deleting Value Overload Function"""
        old_tasks = self.tasks
        self.tasks = []
        for task in old_tasks:
            if key in (task, task.name):
                self.tasks.append(task)

    def __contains__(self, item):
        """`in` Operator Overload Function"""
        for task in self.tasks:
            if item in (task, task.name):
                return True
        return False

    def items(self) -> List[Task]:
        """Get Items"""
        return self.tasks
