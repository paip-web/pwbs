# -*- coding: utf-8 -*-
"""PAiP Web Build System - Configuration and Commands Managers

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from __future__ import print_function
from ..command.command import Command, CommandList
from ..command.command import CommandType, CommandMode, Platform

# Class Definition


class ConfigurationManager(object):
    """Configuration Manager Class"""
    # TODO: Placeholder
    pass


class CommandManager(object):
    """Commands Manager Class"""
    def __init__(self, commands, verbose=1, debug=False):
        """Constructor of the Class
        Args:
            commands: Commands readed from PWBS Commands File
            verbose (int): Verbose Level
                Defaults to Verbose Level 1.
            debug (bool): Debug Mode
                Defaults to False [Disabled Debug Mode].
        """
        # Special Variables
        self.special_vars = [verbose, debug]
        # Commands
        self.commands = commands
        # Time to understand commands
        self.understand()

    def understand(self):
        # TODO: Not good implemented
        result = []
        for cmd_name, cmd in self.commands.items():
            result.append(self.understand_object(cmd_name, cmd))
        self.cmds = CommandList(result)

    def understand_object(self, name, command):
        # TODO: Not good implemented
        if isinstance(command, str):
            # Single Task
            result = Command(
                name,
                CommandType.SingleTask,
                [command],
                "",
                CommandMode.SingleTask_Standard,
                None,
                None,
                Platform.Any)
        elif isinstance(command, list):
            # Multi Task / MultiCommand Legacy
            # TODO: Behaviour to be written
            pass
        elif isinstance(command, dict):
            # Everything
            """
            try:
                Options.append(1)
            except KeyError:
                Options.append(0)
            """
            Options = []
            # Mode
            try:
                mode = command["mode"]
                Options.append(1)
            except KeyError:
                Options.append(0)
            # Commands
            try:
                commands = command["commands"]
                Options.append(1)
            except KeyError as e:
                Options.append(0)
                raise SyntaxError("Commands module in task not found") from e
            # Context
            try:
                context = commands["context"]
                Options.append(1)
            except KeyError:
                Options.append(0)
            # Comment
            try:
                comment = commands["comment"]
                Options.append(1)
            except KeyError:
                Options.append(0)
            args = [
                "",
                CommandType.InitialNullTask,
                [],
                "",
                CommandMode.NullMode,
                None,
                None,
                Platform.Any]
            if Options[0] == 1:
                if mode == "st":  # Single Task
                    args[1] = CommandType.SingleTask
                    args[4] = CommandMode.SingleTask_Standard
                elif mode == "mt":  # Multi Task
                    args[1] = CommandType.MultiTask
                    args[4] = CommandMode.MultiTask_Standard
                elif mode == "mc":  # Multi Command
                    args[1] = CommandType.MultiCommandTask
                    args[4] = CommandMode.MultiCommandTask_Standard
                elif mode == "wc":  # Watcher
                    args[1] = CommandType.WatcherTask
                    args[4] = CommandMode.WatcherTask_StartAndWait
                elif mode == "wc0":  # Watcher
                    args[1] = CommandType.WatcherTask
                    args[4] = CommandMode.WatcherTask_StartAndRun
                elif mode == "s":  # Scheduler
                    args[1] = CommandType.SchedulerTask
                    args[4] = CommandMode.SchedulerTask_StartAndWait
                elif mode == "s0":  # Scheduler
                    args[1] = CommandType.SchedulerTask
                    args[4] = CommandMode.SchedulerTask_StartAndRun
            if Options[1] == 1:
                args[2] = commands
            if Options[2] == 1:
                args[6] = {"context": context}
            if Options[3] == 1:
                args[3] = comment
            result = Command(*args)
        else:
            raise SyntaxError()
        result._log.verbose(self.special_vars[0])
        result._log.debug(self.special_vars[1])
        return result

    def run_task(self, name):
        """Task Runner"""
        return CommandList[name].run()
