#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Build System

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
### Imports
import sys
### From Module Imports
from .__pwbs import print_pref, print_prefix, verboseSpecific
from .pwm.pwm_exec import execute_generator as execute
### Functions
## Single Tasking Interpreter
def singletask_interpreter(task, verbose, commands):
    if isinstance(commands[task], str):
        for output in execute(commands[task]):
            verboseSpecific(verbose, ">0", print, [print_prefix+"Executing Command: {0}".format(commands[task])])
            print(output.decode("utf-8"))
            verboseSpecific(verbose, ">0", print, [print_prefix+"Finished Executing Command"])
        return 0
    else:
        return 1 #Not a Single Task
## Multi Tasking Interpreter
def multitask_interpreter(task, verbose, commands):
    if isinstance(commands[task], list):
        for singletask in commands[task]:
            if isinstance(commands[singletask], str):
                #verboseSpecific(verbose,">=3", print, [print_prefix+"VERBOSE:",commands[task]])
                for output in execute(commands[singletask]):
                    verboseSpecific(verbose, ">0", print, [print_prefix+"Executing Command: {0}".format(commands[singletask])])
                    print(output.decode("utf-8"))
                    verboseSpecific(verbose, ">0", print, [print_prefix+"Finished Executing Command"])
                r = 0
            else:
                r = 1 #Not a Single Task
            if r == 1:
                print(print_prefix+"ERROR[4]: PWBS couldn't find task.")
                return 2 #Errored
        return 0
    else:
        return 1 #Not a Single Task
