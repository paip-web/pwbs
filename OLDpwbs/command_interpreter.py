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
from collections import namedtuple
### From Module Imports
from .__pwbs import print_pref, print_prefix, verboseSpecific, PWBSConfigManager
from . import commands_special as special_commands_module
from . import task_interpreter as task_module
### Placeholders TODO:
special_command = lambda x, y: 1
command = lambda x, y: 1
config = PWBSConfigManager()
plugin_command = lambda x, y: 1
inner_plugin_command = lambda x, y: 1
### Functions
### Special Tasks Interpreter
# TO_TEST: NOT TESTED YET
def special_task_interpreter(arg, verbose, argument_list, iterator):
    global print_prefix
    global config
    special_tasks = {
        "--new-config" : special_commands_module.sc_newconfig, # Argument for creating new config
        "--config" : special_commands_module.sc_config, # Argument to specify which config you want to use
        "--config-version" : lambda: 0, # Argument to specify which config version you want to use [Vars:1,2][Default: 2]
        # That Argument can be used only with existing config
        "--verbose" : special_commands_module.sc_verbose, # Argument to specify which verbose level you want [Vars: 0,1,2,3,255][Default:1]
        "--help" : special_commands_module.sc_help, # Argument to see help
        "--commands-list" : lambda: 0 # Argument to see list of commands in actual config
    }
    ret = None
    r = namedtuple("r", [
        "return_code",
        "err"
    ])
    if arg in special_tasks.keys():
        argument = arg
        verboseSpecific(verbose, ">0", print, [print_prefix+"Running {0} Special Task...".format(argument)])
        verboseSpecific(verbose, ">1", print, [print_prefix+"Received: {0}".format(arg)])
        func_arg = []
        if arg == "--verbose":
            try:
                func_arg = [argument_list[iterator+1]]
                ret = special_tasks[arg](*func_arg)
            except Exception:
                print(print_prefix+"ERROR[2]: PWBS couldn't find parameter")
                ret = r(return_code=2, err=arg)
        elif arg == "--config":
            try:
                func_arg = [argument_list[iterator+1]]
                ret = special_tasks[arg](*func_arg)
                config.reload_JIOnf(ret.filepath, ret.filename)
                verboseSpecific(verbose, ">=3", print, [print_prefix+"VERBOSE:\nFile Path: {0}\nFilename: {1}".format(ret.filepath, ret.filepath)])
            except Exception as e:
                print(print_prefix+"ERROR[2]: PWBS couldn't find parameter")
                #verboseSpecific(verbose,">=3",print, [print_prefix+"ERROR: "+str(e)])
                #verboseSpecific(verbose,">=3",print, [print_prefix+"ERROR: "+e])
                ret = r(return_code=2, err=arg)
        elif arg == "--new-config":
            config = special_tasks[arg](config)
            ret = r(return_code=0, err=0)
        else:
            ret = special_tasks[arg](*func_arg)
        '''PAST:
        r = namedtuple("r", [
            "return_code",
            "err"
        ])
        ret = r(return_code=0, err=arg)
        '''
        verboseSpecific(verbose, ">0", print, [print_prefix+"Finished {0} Special Task...".format(argument)])
    else:
        ret = r(return_code=1, err=arg)
    return ret

### Tasks Interpreter
# TO_TEST: NOT TESTED YET
def normal_task_interpreter(arg, verbose, argument_list, iterator):
    global print_prefix
    global config
    try:
        commands = config.get_commands()
    except Exception as e:
        print(print_prefix + "ERROR[3]: PWBS couldn't find commands")
        #verboseSpecific(verbose,">=3", print, [print_prefix + "ERROR[3]:", str(repr(e))])
        sys.exit(print_prefix + "ERROR[3]: PWBS couldn't find commands")
    ret = None
    r = namedtuple("r", [
        "return_code",
        "err"
    ])
    verboseSpecific(verbose, ">=3", print, [print_prefix+"Commands: {0}".format(str(commands))])
    if arg in commands.keys():
        verboseSpecific(verbose, ">0", print, [print_prefix+"Running {0} Task...".format(arg)])
        singletask = task_module.singletask_interpreter(arg, verbose, commands)
        multitask = task_module.multitask_interpreter(arg, verbose, commands)
        if singletask == 0:
            ret = r(return_code=0, err=0)
        elif singletask == 2: #FAIL
            ret = r(return_code=2, err=0)
        elif multitask == 0:
            ret = r(return_code=0, err=0)
        elif multitask == 2: #FAIL
            ret = r(return_code=2, err=0)
        verboseSpecific(verbose, ">0", print, [print_prefix+"Finished {0} Task...".format(arg)])
    else:
        ret = r(return_code=1, err=arg)
    return ret

### Main Command Interpreter
# TO_TEST: NOT TESTED YET
def command_interpreter(args, verbose):
    global config
    skip = 0
    _a = config.try_load()
    if (_a == False) and (not("--config" in args)):
        print(print_prefix + "ERROR[F1]: PWBS couldn't read default configuration file [pwbs.json] and couldn't find --config option.")
        sys.exit(print_prefix + "ERROR[F1]: PWBS couldn't read default configuration file [pwbs.json] and couldn't find --config option.")
    for i, arg in enumerate(args):
        if skip > 0:
            skip -= 1
            continue
        sti = special_task_interpreter(arg, verbose, args, i)
        cti = normal_task_interpreter(arg, verbose, args, i)
        ipgi = inner_plugin_command(arg, verbose)
        pci = plugin_command(arg, verbose)
        verboseSpecific(verbose, ">=3", print, ["{0}Command Interpreter:\n{0}Skip Value: {1}\n{0}Special Task Interpreter Return: {2}\n{0}Command Task Interpreter Return: {3}\n{0}Inner Plugin Command Interpreter: {4}\n{0}Plugin Command Interpreter: {5}\n{0}Verbose Level: {6}".format(
            print_prefix,
            skip,
            sti,
            cti,
            ipgi,
            pci,
            verbose
        )])
        if sti.return_code == 0: #SUCCESS BRANCH
            try:
                verbose = sti.verbose_mode
            except AttributeError:
                pass
            try:
                skip = sti.skip_args
            except AttributeError:
                pass
            continue
        elif sti.return_code == 2: #ERROR BRANCH
            continue
        elif cti.return_code == 0: #SUCCESS BRANCH
            continue
        elif cti.return_code == 2: #ERROR BRANCH
            continue
        elif ipgi == 0: #SUCCESS BRANCH
            continue
        elif ipgi == 2: #ERROR BRANCH
            continue
        elif pci == 0: #SUCCESS BRANCH
            continue
        elif pci == 2: #ERROR BRANCH
            continue
        else:
            print(print_prefix+"ERROR[1]: PWBS couldn't find specified task.")
            print(print_prefix+"ERROR[1]: Not Found Task:", arg)
            continue
