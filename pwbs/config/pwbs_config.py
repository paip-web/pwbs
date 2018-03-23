# -*- coding: utf-8 -*-
"""PAiP Web Build System - PWBS Config Manager

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from __future__ import print_function
from ..log.logger import Logger
from .config_manager import ConfigManager
from ..command.command import Command, CommandList
from ..command.command import CommandType, Platform, CommandMode

# Class Definition


class PWBS_ConfigManager(object):
    """PWBS Config Class"""
    def __init__(self):
        """Constructor of the Class"""
        # Variables
        """Logger"""
        self.log = Logger()
        """Verbose Level"""
        self.verbose = 1
        """Debug Mode"""
        self.debug = False
        """Config File Manager"""
        self.configmanager = ConfigManager()
        """Commands"""
        self.commands = CommandList([])
        # Constructor Methods
        self.config_file()

    def config_file(self):
        """Config File Function
        Returns:
            JSON Object from Config File
        """
        self.log.log_debug("Loading Configuration File Data...")
        data = self.configmanager.load()
        self.log.log_debug("Configuration File Data Loaded.")
        return data

    def commands_to_commandlist(self):
        commands = []
        for name, body in self.config_file().items():
            if isinstance(body, str):
                # Single Task
                commands.append(Command(
                    name,
                    CommandType.SingleTask,
                    [body],
                    mode=CommandMode.SingleTask_Standard))
            elif isinstance(body, list):
                # TODO: Multi Task
                pass
            else:
                # Everything Else
                try:
                    cmdtype = PWBS_ConfigManager.ctcl__cmdtype(body)
                except KeyError:
                    cmdtype = CommandType.ErrorTask
                try:
                    comment = PWBS_ConfigManager.ctcl__comment(body)
                except KeyError:
                    comment = ""
                try:
                    cmdmode = PWBS_ConfigManager.ctcl__cmdmode(body)
                except KeyError:
                    cmdmode = CommandMode.ErrorTask_ErrorMode
                try:
                    commands = PWBS_ConfigManager.ctcl__commands(body)
                except KeyError:
                    commands = None
                try:
                    arguments = PWBS_ConfigManager.ctcl__arguments(body)
                except KeyError:
                    arguments = None
                try:
                    platform = PWBS_ConfigManager.ctcl__platform(body)
                except KeyError:
                    platform = Platform.Any
                commands.append(Command(
                    name,
                    cmdtype,
                    commands,
                    comment,
                    cmdmode,
                    arguments,
                    None,
                    platform))
        self.commands = CommandList(commands)

    def ctcl__cmdtype(commandbody):
        ct = commandbody["mode"]
        if ct == "st":
            return CommandType.SingleTask
        elif ct == "mt":
            return CommandType.MultiTask
        elif ct == "mc":
            return CommandType.MultiCommandTask
        elif ct == "wc0" or ct == "wc":
            return CommandType.WatcherTask
        elif ct == "sc0" or ct == "sc":
            return CommandType.SchedulerTask
        return CommandType.ErrorTask

    def ctcl__comment(commandbody):
        return commandbody["comment"]

    def ctcl__cmdmode(commandbody):
        ct = commandbody["mode"]
        if ct == "st":
            return CommandMode.SingleTask_Standard
        elif ct == "mt":
            return CommandMode.MultiTask_Standard
        elif ct == "mc":
            return CommandMode.MultiCommandTask_Standard
        elif ct == "wc0":
            return CommandMode.WatcherTask_StartAndRun
        elif ct == "wc":
            return CommandMode.WatcherTask_StartAndWait
        elif ct == "sc0":
            return CommandMode.SchedulerTask_StartAndRun
        elif ct == "sc":
            return CommandMode.SchedulerTask_StartAndWait
        return CommandMode.ErrorTask_ErrorMode

    def ctcl__arguments(commandbody):
        return commandbody["context"]

    def ctcl__commands(commandbody):
        return commandbody["commands"]

    def ctcl__platform(commandbody):
        ct = commandbody["platform"]
        if isinstance(ct, int):
            return Platform(ct)
        elif isinstance(ct, str):
            if ct.lower() == "windows" or ct.lower() == "win":
                return Platform.Windows
            elif ct.lower() == "linux" or ct.lower() == "lin":
                return Platform.Linux
            elif ct.lower() == "macos":
                return Platform.MacOS
            elif ct.lower() == "macosx":
                return Platform.MacOS
            elif ct.lower() == "mac":
                return Platform.MacOS
            else:
                return Platform.Other
        else:
            raise ValueError("Not Supported Type for that operation")
