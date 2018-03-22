# -*- coding: utf-8 -*-
"""PAiP Web Build System - Command Class

This module contains Command Class and other classes needed by Command Class.
Command Class is for making Command [Tasks] as easy as possible.

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
    """Command Type Enum
    This enum is for specifying Command Type in the Command Class.
    """
    # DEV: 0xABB | A - Type | B - Number

    """Null Task"""
    NullTask = 0x000
    """Initial Value - Null Task Type"""
    InitialNullTask = 0x001
    """Special Tasks (like --help)"""
    SpecialTask = 0x101
    # NOT_IMPLEMENTED:
    # """Internal Plugin Task
    # [Plugin task from plugin bultin in PWBS]"""
    # InternalPluginTask = 0x102
    # NOT_IMPLEMENTED:
    # """Plugin Task
    # [Plugin task from plugin written in Python using PWBS Public API]"""
    # PluginTask = 0x103
    # NOT_IMPLEMENTED:
    # """JSON Plugin Task
    # [Plugin task from plugin written in JSON using PWBS JSON Plugin File]"""
    # JSONPluginAPIPlugin = 0x104
    """Single Task
    [One Run = One Shell Command]"""
    SingleTask = 0x201
    """Multi Task
    [One Run = Multiple Tasks]"""
    MultiTask = 0x202
    """Multi Command Task
    [One Run = Multiple Shell Commands]"""
    MultiCommandTask = 0x203
    """Watcher Task"""
    WatcherTask = 0x204
    """Scheduler Task"""
    SchedulerTask = 0x205
    """Test Task
    [For Testing Purposes]"""
    TestTask = 0xFF0
    """Error Task
    [For Error Catching Purposes]"""
    ErrorTask = 0xFF1
    """Null Task"""
    NullTaskF = 0xFFF


class Platform(Enum):
    """Platform Enum
    This enum is to specify platform command is for.
    """
    """Null"""
    NullOS = 0b0000
    """Windows"""
    Windows = 0b0001
    """Linux"""
    Linux = 0b0010
    """Mac OS X"""
    MacOS = 0b0100
    """Any OS not specified above"""
    Other = 0b1000
    """Any OS [default]"""
    Any = 0b1111


class CommandMode(Enum):
    """Command Mode Enum
    This enum is to specify in what mode Command have to run.
    """
    # DEV: 0xABBBCDDD | A - Type | B - Task Type | C - Mode Type | D - Number
    # Task Modes
    """Single Task - Standard Mode"""
    SingleTask_Standard = 0x22010001
    """Multi Task - Standard Mode"""
    MultiTask_Standard = 0x22020001
    """Multi Command Task - Standard Mode"""
    MultiCommandTask_Standard = 0x22030001
    """Watcher Task - Run First Mode"""
    WatcherTask_StartAndRun = 0x22040001
    """Watcher Task - Wait First Mode"""
    WatcherTask_StartAndWait = 0x22040002
    """Scheduler Task - Run First Mode"""
    SchedulerTask_StartAndRun = 0x22050001
    """Scheduler Task - Wait First Mode"""
    SchedulerTask_StartAndWait = 0x22050002
    # Special and Control Modes
    """Null Mode
    [For Testing Purposes]"""
    NullMode = 0x00000000
    """Mode Not Specified
    [For Error Catching Purposes]"""
    ModeNotSpecified = 0x00000001
    """Test Task - Test Mode
    [For Testing Purposes]"""
    TestTask_TestMode = 0xFFF00000
    """Error Task - Error Mode
    [For Error Catching Purposes]"""
    ErrorTask_ErrorMode = 0xFFF1FFFF
    """Null Task - Null Mode
    [For Testing Purposes]"""
    NullTask_NullMode = 0xF000FFF0
    """Null Task - Null Mode
    [For Testing Purposes]"""
    NullTaskF_NullMode = 0xFFFFFFF0
    """Error Mode
    [For Error Catching Purposes]"""
    ErrorMode = 0xFFFFFFFF


class Command(object):
    """Command Class
    This class is for making Commands [Tasks].
    This class is for making Commands File Interpreter too.
    """
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
        """Constructor of the Class
        Args:
            name: Name of the Command [Task]
            cmd_type (:obj:`CommandType`): Type of the Command [Task]
                Defaults to Initial Null Task.
            commands (list): List of Commands what Command should do on run
                Defaults to None.
            comment (:obj:`str`): Comment of Command
                Defaults to Empty String
            mode (:obj:`CommandType`): Mode of the Command [Task]
                Defaults to NullMode.
            arguments (dict): Arguments of the Command [Task]
                Defaults to None.
            special (dict): Special Arguments of the Command [Task]
                Defaults to None.
            platform (:obj:`Platform`): Platform of the Command [Task]
                Defaults to Any Platform.
        """
        # Control Vars
        """Logger Variable"""
        self._log = Logger()
        # Defining Variables
        """Name of the Command"""
        self.name = name
        """Type of the Command"""
        self.type = cmd_type
        """List of Commands what Command should do on run"""
        self.commands = commands
        """Comment of Command"""
        self.comment = comment
        """Mode of the Command"""
        self.mode = mode
        """xArguments of the Command"""
        self.arguments = arguments
        """Special Arguments of the Command"""
        self.special = special
        """Platform of the Command"""
        self.platform = platform

    def __eq__(self, other):
        """Equation Operator Overload Function"""
        # Comparing names if it's Command Class
        if isinstance(other, Command):
            return self.name == other.name
        # Comparing name to other value if it's not Command Class
        return self.name == other

    def run(self):
        """Run Function of Command"""
        # Type Checking and running special function for type
        if self.type is CommandType.SingleTask:
            # Single Task
            self.execute_as_singletask_or_multicommand()
        elif self.type is CommandType.MultiCommandTask:
            # Multi Command Task
            self.execute_as_singletask_or_multicommand()
        elif self.type is CommandType.WatcherTask:
            # Watcher Task
            self.execute_as_watcher()
        elif self.type is CommandType.SchedulerTask:
            # Scheduler Task
            self.execute_as_scheduler()
        elif self.type is CommandType.TestTask:
            # Test Task
            return "TESTED"
        elif self.type is CommandType.ErrorTask:
            # Error Task
            raise Exception("Error Task Reached!")
        elif self.type is CommandType.NullTask:
            # Null Task - Debug
            self._log.log_verbose("NullTask Reached!", 2)
        elif self.type is CommandType.NullTaskF:
            # Null Task - Debug
            self._log.log_verbose("NullTask Reached!", 2)
        elif self.type is CommandType.InitialNullTask:
            # Null Task - Debug
            self._log.log_verbose("NullTask Reached!", 2)
        elif self.type is CommandType.MultiTask:
            # Multi Task
            # TODO: Make that behaviour however
            # DEV: Need a loop of runs or something
            pass
        else:
            # Error Case
            self._log.log_verbose("Task not implemented or broken!", 0)
            raise NotImplementedError("Task is Not Implemented or Broken!")
        return None

    def execute_as_singletask_or_multicommand(self):
        """Single Task and Multi Command Task Runner"""
        # Log Starting Run
        self._log.log_verbose("Running {0} Task...".format(self.name), 1)
        # Loop in Commands and their output
        for cmd_in, cmd_out in zip(
                self.commands,
                execute_generator(self.commands)):
            # Log Execute
            self._log.log_verbose('Executing "{0}"...'.format(cmd_in), 2)

            def prefixer(text):
                """Custom prefixer function needed only in that function"""
                return "[{0}]: {1}".format(
                    datetime.now().strftime("%H:%M:%S"),
                    text)
            # Log Output
            self._log.log(
                cmd_out.decode("utf-8"),
                prefixer)
        # Log Finish
        self._log.log_verbose("Finished {0} Task...".format(self.name), 1)

    def execute_as_watcher(self):
        """Watcher Task Runner"""
        # TODO: To be written
        pass

    def execute_as_scheduler(self):
        """Scheduler Task Runner"""
        # TODO: To be written
        pass

    def __add__(self, other):
        """Addition Operator Overload Function"""
        # Asserting that both of objects is Command Class objects
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
    """Command List Class
    This class is to make custom list type for Command Class.
    """
    def __init__(self, value: Command) -> None:
        """Constructor of the Class"""
        self.values = value

    def __getitem__(self, key):
        """Dictionary Based Getting Value Overload Function"""
        for i in self.values:
            if i == key or i.name == key:
                return i
        raise KeyError("Key not found!")

    def __setitem__(self, key, value):
        """Dictionary Based Setting Value Overload Function"""
        oldvalues = self.values
        self.values = []
        for i in oldvalues:
            if i == key or i.name == key:
                self.values.append(value)
            else:
                self.values.append(i)

    def __delitem__(self, key):
        """Dictionary Based Deleting Value Overload Function"""
        oldvalues = self.values
        self.values = []
        for i in oldvalues:
            if i != key and i.name != key:
                self.values.append(i)

    def __contains__(self, item):
        """`in` Operator Overload Function"""
        for i in self.values:
            if i == item or i.name == item:
                return True
        return False
