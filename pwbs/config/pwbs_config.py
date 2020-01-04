# -*- coding: utf-8 -*-
"""PAiP Web Build System - PWBS Config Manager

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from __future__ import print_function
from pwbs.log.logger import Logger
from pwbs.config.config_manager import ConfigManager, PWBSInvalidConfigFile
from pwbs.command.command import Command, CommandList
from pwbs.command.command import CommandType, Platform, CommandMode
# Class Definition


class PWBS_ConfigManager:
    """PWBS Config Class"""
    @staticmethod
    def commands_to_commandlist(config_data):
        commands = []
        """Testing for invalid Configuration File"""
        try:
            assert config_data["commands"] is not None
        except AssertionError as e:
            raise PWBSInvalidConfigFile("Invalid Configuration File") from e
        except KeyError as e:
            raise PWBSInvalidConfigFile("Invalid Configuration File") from e
        """Loop of creating Commands"""
        for name, body in config_data["commands"].items():
            if isinstance(body, str):
                # Single Task
                commands.append(Command(
                    name,
                    CommandType.SingleTask,
                    [body],
                    mode=CommandMode.SingleTask_Standard))
            elif isinstance(body, list):
                # TODO: Multi Task
                # from ..core import NotImplementedFeatureError
                # raise NotImplementedFeatureError("Not Implemented Feature Called")
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
                    cmds = PWBS_ConfigManager.ctcl__commands(body)
                except KeyError:
                    cmds = None
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
                    cmds,
                    comment,
                    cmdmode,
                    arguments,
                    None,
                    platform))
        return CommandList(commands)

    @staticmethod
    def ctcl__cmdtype(commandbody):
        ct = commandbody["mode"]
        if ct == "st":
            return CommandType.SingleTask
        if ct == "mt":
            return CommandType.MultiTask
        if ct == "mc":
            return CommandType.MultiCommandTask
        if ct in ("wc0", "wc"):
            return CommandType.WatcherTask
        if ct in ("sc0", "sc"):
            return CommandType.SchedulerTask
        return CommandType.ErrorTask

    @staticmethod
    def ctcl__comment(commandbody):
        return commandbody["comment"]

    @staticmethod
    def ctcl__cmdmode(commandbody):
        ct = commandbody["mode"]
        if ct == "st":
            return CommandMode.SingleTask_Standard
        if ct == "mt":
            return CommandMode.MultiTask_Standard
        if ct == "mc":
            return CommandMode.MultiCommandTask_Standard
        if ct == "wc0":
            return CommandMode.WatcherTask_StartAndRun
        if ct == "wc":
            return CommandMode.WatcherTask_StartAndWait
        if ct == "sc0":
            return CommandMode.SchedulerTask_StartAndRun
        if ct == "sc":
            return CommandMode.SchedulerTask_StartAndWait
        return CommandMode.ErrorTask_ErrorMode

    @staticmethod
    def ctcl__arguments(commandbody):
        return commandbody["context"]

    @staticmethod
    def ctcl__commands(commandbody):
        return commandbody["commands"]

    @staticmethod
    def ctcl__platform(commandbody):
        ct = commandbody["platform"]
        if isinstance(ct, int):
            return Platform(ct)
        if isinstance(ct, str):
            if ct.lower() in ("windows", "win"):
                return Platform.Windows
            if ct.lower() in ("linux", "lin"):
                return Platform.Linux
            if ct.lower() in ("macos", "macosx", "mac"):
                return Platform.MacOS
            return Platform.Other
        raise ValueError("Not Supported Type for that operation")
