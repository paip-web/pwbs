# -*- coding: utf-8 -*-
"""PAiP Web Build System - Task Factory Class

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from typing import Dict
from pwbs.tasks.task_list import TaskList
from pwbs.tasks.task_config import TaskConfig
from pwbs.tasks.task_constants import TaskConstants
from pwbs.core.error_messages import ErrorMessages
from pwbs.core import service_manager
from pwbs.core import UserError

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

task_factory_map = {}


class TaskFactory:
    """Task Factory Class"""

    @staticmethod
    def make(config=None, *args):
        """Make Task Object"""
        if not isinstance(config, TaskConfig):
            config = TaskConfig(config)
        task_mode = config.mode
        if task_mode not in task_factory_map.keys():
            raise NotImplementedError(ErrorMessages.task_mode_not_implemented(task_mode))
        return task_factory_map[task_mode](config, *args)

    @staticmethod
    def make_config_from_json_task(name: str, json_config: Dict = None) -> TaskConfig:
        """Make Task Configuration from JSON Configuration Data"""
        task_config = TaskConfig()
        task_config.name = name
        if isinstance(json_config, str):
            task_config.mode = TaskConstants.task_mode().single_task()
            task_config.commands = [json_config]
        elif isinstance(json_config, list):
            task_config.mode = TaskConstants.task_mode().multi_task()
            task_config.extends = ','.join(json_config)
        elif isinstance(json_config, dict):
            task_config = TaskConfig(json_config)
            task_config.name = name
        else:
            raise NotImplementedError('Wrong Configuration')
        return task_config

    @staticmethod
    def make_list(config, *args):
        """Make Task List"""
        tasks = []
        for name, body in config.items():
            try:
                task_config = TaskFactory.make_config_from_json_task(name, body)
                tasks.append(TaskFactory.make(task_config, *args))
            except NotImplementedError as e:
                service_manager['log'].log_error(UserError(ErrorMessages.task_skipped(name)))
                service_manager['log'].log_error(e)
        return TaskList(tasks)
