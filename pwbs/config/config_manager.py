# -*- coding: utf-8 -*-
"""PAiP Web Build System - Config Manager

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from __future__ import print_function
from os import getcwd
from ..lib.pwm.pwm_json import JSON_IO
from ..lib.pwm.pwm_system import SystemVersion

# Class Definition


# TO_TEST:
class ConfigManager(object):
    """Config Manager Class"""
    def __init__(self):
        self.config_filename = "pwbs.json"
        cwd = getcwd()
        if SystemVersion().system_system == "Windows":
            self.config_filename_path = cwd+"\\"+self.config_filename
        else:
            self.config_filename_path = cwd+"/"+self.config_filename
        self.filemanager = JSON_IO(self.config_filename_path)
        self.file_load()
        self.load()

    def file_load(self):
        self.config_text = self.filemanager.read()
        return self.config_text

    def load(self):
        self.config_dict = dict(self.file_load())
        return self.config_dict

    def write(self, newdata):
        return self.filemanager.write(newdata)
