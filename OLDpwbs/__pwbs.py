#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Build System

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
### Imports
from datetime import datetime
import re
from os import getcwd
from .pwm.pwm_json import JSON_IO
from .pwm.pwm_system import SystemVersion
### Functions and Variables
print_prefix = "PWBS[{0}]: ".format(datetime.now().strftime("%H:%M:%S"))
def print_pref():
    return print_prefix

def verboseSpecific(verbose, level, function, arg=[]):
    if eval(str(verbose)+str(level)):
        return function(*arg)
    else:
        return 0xFF

def regexString(string, regex):
    pattern = re.compile(regex)
    return pattern.match(string)

class PWBSConfigManager:
    def __init__(self):
        cwd = getcwd()
        self.filename = "pwbs.json"
        if SystemVersion().system_system == "Windows":
            path_to_file = cwd+"\\"+self.filename
        else:
            path_to_file = cwd+"/"+self.filename
        self.filepath = path_to_file
        self.config_data = {}
        self.JSONIO = JSON_IO(self.filepath)
    def reload_JSONIO(self):
        self.JSONIO = JSON_IO(self.filepath)
    def reload_JIOnf(self, newfilepath, newfilename):
        self.filename = newfilename
        self.filepath = newfilepath
        return self.reload_JSONIO()
    def reload(self):
        self.reload_JSONIO()
        self.config_data = self.JSONIO.read()
        return self.config_data
    def update(self, newdata):
        self.JSONIO.write(newdata)
        self.config_data = self.JSONIO.read()
        return self.config_data
    def try_load(self):
        try:
            self.reload()
            return True
        except Exception:
            print(print_prefix+"ERROR[F0]: PWBS couldn't read default configuration file [pwbs.json].")
            return False
    def init_config(self):
        data = {
            "commands" : {
            }
        }
        return self.update(data)
    def get_commands(self):
        self.reload()
        return self.config_data["commands"]
