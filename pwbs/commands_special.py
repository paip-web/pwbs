#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Build System - Special Commands

NAME - PAiP Web Build System - Special Commands
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
### Imports
from collections import namedtuple
from os import getcwd
### From Module Imports
from .__pwbs import print_pref, print_prefix, verboseSpecific
### Functions
# TO_TEST: NOT TESTED YET
def sc_help():
    global print_prefix
    print(print_prefix+"Help for PWBS")
    print(
        "This software is in pre-alpha so not everything might be implemented yet.", # PAST: To Change in future versions
        "You can see which things are and aren't in actual version of software by flags", # PAST: To Change in future versions
        "Usage:",
        "pwbs [options] [task]",
        "Options:",
        "--new-config                       # Option to make new config file [pwbs.json]",
        "--config [file]                    # Option to specify which existing config you want to use",
        "--config-version [version]         # NOT_IMPLEMENTED:Option to specify which version of config you want to use",
        "       # Version \"1\": Used with older PWBS gitlab:/paipweb/paip-web-build-system",
        "       # Now good too but limited [good by simpler file]",
        "       # Version \"2\": [Default]Actual Version of Config",
        "--verbose [level]                  # Option to specify which verbose level you want",
        "       # Mode \"0\": No Verbose | Small Information about running",
        "       # Mode \"1\": [Default] Small Verbose | Some Information about what's going on",
        "       # Mode \"2\": Medium Verbose | Information about running and some about processes under the hood",
        "       # Mode \"3\": Full Verbose | Much Information about running and processes under the hood",
        "       # NOT_IMPLEMENTED:FUTURE:Mode \"255\": Extreme Verbose Mode | Information about everything",
        "--help                             # Option to see this message",
        "--commands-list                    # NOT_IMPLEMENTED:Option to see list of commands in actual config",
        "--deamonize                        # NOT_IMPLEMENTED:Option to make deamon in linux or service in windows working from start of system",
        "",
        "Features:",
        "* Single Tasking",
        "* Multi Tasking",
        "* NOT_IMPLEMENTED:Multi Command",
        "* NOT_IMPLEMENTED:Watcher",
        "* NOT_IMPLEMENTED:Scheduler",
        "* NOT_IMPLEMENTED:PWBS Inner Plugin",
        "* NOT_IMPLEMENTED:PWBS Python Plugins",
        "* NOT_IMPLEMENTED:PWBS JSON Plugins",
        "* NOT_IMPLEMENTED:Support Legacy for Old PWBS",
        "* NOT_IMPLEMENTED:Support Commented Tasks",
        ""
        , sep='\n')
    base = namedtuple("base", ["return_code", "err"])
    return base(return_code=0, err=0)
# TO_TEST: NOT TESTED YET
def sc_verbose(new_verbose):
    global print_prefix
    print(print_prefix+"Changing Verbose Mode")
    base = namedtuple("base", ["return_code", "err", "verbose_mode", "skip_args"])
    return base(return_code=0, err=0, verbose_mode=new_verbose, skip_args=1)

def sc_config(newfilename):
    global print_prefix
    print(print_prefix+"Changing Config File to {0}".format(newfilename))
    cwd = getcwd()
    base = namedtuple("base", ["return_code", "err", "skip_args", "filepath", "filename"])
    return base(return_code=0, err=0, filename=newfilename, filepath="{0}/{1}".format(cwd, newfilename), skip_args=1)
    #return (newfilename, "{0}/{1}".format(cwd, newfilename)) # PAST: Deleted

def sc_newconfig(configManager):
    global print_prefix
    print(print_prefix+"Initializing Config File")
    newconfig = configManager
    newconfig.init_config()
    return newconfig
