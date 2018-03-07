# -*- coding: utf-8 -*-
"""PAiP Web Build System - Command Class

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from __future__ import print_function
from enum import Enum
from datetime import datetime
from ..lib.pwm.pwm_exec import execute_generator
from ..log.logger import Logger

# Class Definition


class CommandType(Enum):
    """Command Type Enum"""
    # 0xABB | A - Type | B - Number
    NullTask = 0x000
    InitialNullTask = 0x001
    SpecialTask = 0x101
    # NOT_IMPLEMENTED:InternalPluginTask = 0x102
    # NOT_IMPLEMENTED:PluginTask = 0x103
    # NOT_IMPLEMENTED:JSONPluginAPIPlugin = 0x104
    SingleTask = 0x201
    MultiTask = 0x202
    MultiCommandTask = 0x203
    WatcherTask = 0x204
    SchedulerTask = 0x205
    TestTask = 0xFF0
    ErrorTask = 0xFF1
    NullTaskF = 0xFFF


class Platform(Enum):
    """Platform Enum"""
    NullOS = 0b0000
    Windows = 0b0001
    Linux = 0b0010
    MacOS = 0b0100
    Other = 0b1000
    Any = 0b1111


class CommandMode(Enum):
    """Command Mode Enum"""
    # 0xABBBCDDD | A - Type | B - Task Type | C - Mode Type | D - Number
    # Task Modes
    SingleTask_Standard = 0x22010001
    MultiTask_Standard = 0x22020001
    MultiCommandTask_Standard = 0x22030001
    WatcherTask_StartAndRun = 0x22040001
    WatcherTask_StartAndWait = 0x22040002
    SchedulerTask_StartAndRun = 0x22050001
    SchedulerTask_StartAndWait = 0x22050002
    # Special and Control Modes
    NullMode = 0x00000000
    ModeNotSpecified = 0x00000001
    TestTask_TestMode = 0xFFF00000
    ErrorTask_ErrorMode = 0xFFF1FFFF
    NullTask_NullMode = 0xF000FFF0
    NullTaskF_NullMode = 0xFFFFFFF0
    ErrorMode = 0xFFFFFFFF


class Command(object):
    """Command Class"""
    def __init__(
            self,
            name,
            cmd_type: CommandType = CommandType.InitialNullTask,
            commands: list = None,
            comment: str = "",
            mode: CommandMode = CommandMode.NullMode,
            arguments: dict = None,
            special: dict = None,
            platform: Platform = Platform.Any) -> None:
        # Control Vars
        self._log = Logger()
        # Defining Variables
        self.name = name
        self.type = cmd_type
        self.commands = commands
        self.comment = comment
        self.mode = mode
        self.arguments = arguments
        self.special = special
        self.platform = platform

    def __eq__(self, other):
        if isinstance(other, Command):
            return self.name == other.name
        return self.name == other

    def run(self):
        if self.type is CommandType.SingleTask:
            self.execute_as_singletask_or_multicommand()
        elif self.type is CommandType.MultiCommandTask:
            self.execute_as_singletask_or_multicommand()
        elif self.type is CommandType.WatcherTask:
            self.execute_as_watcher()
        elif self.type is CommandType.SchedulerTask:
            self.execute_as_scheduler()
        elif self.type is CommandType.TestTask:
            return "TESTED"
        elif self.type is CommandType.ErrorTask:
            raise Exception("Error Task Reached!")
        elif self.type is CommandType.NullTask:
            self._log.log_verbose("NullTask Reached!", 2)
        elif self.type is CommandType.NullTaskF:
            self._log.log_verbose("NullTask Reached!", 2)
        elif self.type is CommandType.InitialNullTask:
            self._log.log_verbose("NullTask Reached!", 2)
        elif self.type is CommandType.MultiTask:
            # TODO: Make that behaviour however
            pass
        else:
            self._log.log_verbose("Task not implemented or broken!", 0)
            raise NotImplementedError("Task is Not Implemented or Broken!")
        return None

    def execute_as_singletask_or_multicommand(self):
        self._log.log_verbose("Running {0} Task...".format(self.name), 1)
        for cmd_in, cmd_out in zip(
                self.commands,
                execute_generator(self.commands)):
            self._log.log_verbose('Executing "{0}"...'.format(cmd_in), 2)

            def prefixer(text):
                return "[{0}]: {1}".format(
                    datetime.now().strftime("%H:%M:%S"),
                    text)
            self._log.log(
                cmd_out.decode("utf-8"),
                prefixer)
        self._log.log_verbose("Finished {0} Task...".format(self.name), 1)

    def execute_as_watcher(self):
        # TODO: To be written
        pass

    def execute_as_scheduler(self):
        # TODO: To be written
        pass

    def __add__(self, other):
        assert isinstance(other, Command)
        # This is for multitask
        # Changing Type and Mode to MultiTask
        self.type = CommandType.MultiTask
        self.mode = CommandMode.MultiTask_Standard
        self.commands.append(other.commands)
        self.platform = self.platform | other.platform
        self.arguments += other.arguments
        self.special += other.special
        # Returning result
        return self


class CommandList(object):
    """Command List Class"""
    def __init__(self, value: Command) -> None:
        self.values = value

    def __getitem__(self, key):
        for i in self.values:
            if i == key or i.name == key:
                return i
        raise KeyError("Key not found!")

    def __setitem__(self, key, value):
        oldvalues = self.values
        self.values = []
        for i in oldvalues:
            if i == key or i.name == key:
                self.values.append(value)
            else:
                self.values.append(i)

    def __delitem__(self, key):
        oldvalues = self.values
        self.values = []
        for i in oldvalues:
            if i != key and i.name != key:
                self.values.append(i)

    def __contains__(self, item):
        for i in self.values:
            if i == item or i.name == item:
                return True
        return False
