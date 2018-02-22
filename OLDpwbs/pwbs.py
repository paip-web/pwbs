#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Build System

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
### Imports
import sys
from os import path, getcwd
### From Module Imports
from .pwm.pwm_system import SystemVersion
from .command_interpreter import print_prefix
### Functions
# TO_TEST: NOT TESTED YET
def baner(version, verbose, args):
    """Baner PWBS"""
    global print_prefix
    print("PAiP Web Build System v" + version)
    if verbose == 0:
        return 0
    elif verbose == 1:
        v = SystemVersion()
        print("PWBS Running in {0} v.{1} [{2}] on {3} with {4} {5} [{6}]".format(
            v.python_implementation,
            v.python_version,
            v.python_compiler,
            v.network_name,
            v.system_system,
            v.system_version,
            v.machine
        ))
        print(print_prefix+"Starting...")
    elif verbose == 2:
        v = SystemVersion()
        print(print_prefix+"Showing system information")
        print("-----------------------------------")
        print("Machine Spec")
        print("-----------------------------------")
        print("Network: {0}\nProcessor Name: {1}\nPython: {2} v.{3} [{4}]\nOperating System: {5} {6} [{7}]\nType: {8}".format(
            v.network_name,
            v.processor_name,
            v.python_implementation,
            v.python_version,
            v.python_compiler,
            v.system_system,
            v.system_release,
            v.system_version,
            v.machine
        ))
        print("-----------------------------------")
        print(print_prefix+"Starting...")
    elif verbose == 3:
        v = SystemVersion()
        print(print_prefix+"Showing system information")
        print("-----------------------------------")
        print("Machine Spec")
        print("-----------------------------------")
        print("Network: {0}\nProcessor Name: {1}\nPython: {2} v.{3} [{4}]\nOperating System: {5} {6} [{7}]\nType: {8}".format(
            v.network_name,
            v.processor_name,
            v.python_implementation,
            v.python_version,
            v.python_compiler,
            v.system_system,
            v.system_release,
            v.system_version,
            v.machine
        ))
        print("-----------------------------------")
        print("Run Spec")
        print("-----------------------------------")
        print("Script Directory: {0}\nCurrent Working Directory: {1}\nCLI Arguments: {2}".format(
            path.abspath(path.dirname(__file__)),
            getcwd(),
            str(args)
        ))
        print("-----------------------------------")
        print(print_prefix+"Starting...")
    elif verbose == 255:
        #TODO: Good Ideas Needed
        pass
