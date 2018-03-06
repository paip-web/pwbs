#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Module - Execute Commands

This module creates function to call command line commands.

NAME - PAiP Web Module - Execute Commands
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
VERSION - v.0.0.0.4
"""
# TODO: MAKE MORE COMPLEX THAT SCRIPT [GENERATOR VERSION]
def execute(command):
    """Function to execute command line commands

    Args:
        command (object): Command

    Returns:
        :obj:`str`: Returning Output of Command
    """
    from subprocess import run, PIPE
    if isinstance(command, list):
        retval = ""
        for cmd in command:
            retval += str(run(cmd, shell=True, stdout=PIPE).stdout)
        return retval
    else:
        return run(command, shell=True, stdout=PIPE).stdout


def execute_generator(command):
    """Function to execute command line commands in generator style

    Args:
        command (object): Command

    Yields:
        :obj:`str`: Returning Output of Command
    """
    from subprocess import run, PIPE
    if isinstance(command, list):
        for cmd in command:
            yield run(cmd, shell=True, stdout=PIPE).stdout
    else:
        yield run(command, shell=True, stdout=PIPE).stdout
