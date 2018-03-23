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


class ConfigManager(object):
    """Config Manager Class
    This class is for Managing Config File.
    """
    def __init__(self, filename="pwbs.json"):
        """Constructor of the class"""
        """Configuration File Name"""
        self.config_filename = filename
        # Getting path of configuration file
        cwd = getcwd()
        if SystemVersion().system_system == "Windows":
            """Configuration File Path"""
            self.config_filename_path = cwd+"\\"+self.config_filename
        else:
            """Configuration File Path"""
            self.config_filename_path = cwd+"/"+self.config_filename
        """Configuration File Manager"""
        self.filemanager = JSON_IO(self.config_filename_path)
        # Preloading File
        self.load()

    def load(self):
        """Configuration Loader
        Reading JSON from Config File and Converting to Dict.
        """
        self.config_dict = dict(self.filemanager.read())
        return self.config_dict

    def write(self, newdata):
        """Configuration Writer
        Writing JSON to Config File.
        Args:
            newdata: New Data for the Config File.
        """
        return self.filemanager.write(newdata)
