#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Module - Execute Commands

This module creates function to call command line commands.

NAME - PAiP Web Module - Execute Commands
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
VERSION - v.0.0.0.3
"""
def execute(command):
    """Function to execute command line commands

    Args:
        command (object): Command

    Returns:
        :obj:`str`: Returning Output of Command
    """
    from subprocess import run
    if isinstance(command, list):
        retval = ""
        for cmd in command:
            retval += str(run(cmd, shell=True).stdout)
        return retval
    else:
        return run(command, shell=True).stdout
