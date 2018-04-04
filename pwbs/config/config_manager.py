# -*- coding: utf-8 -*-
"""PAiP Web Build System - Config Manager

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from __future__ import print_function
from os import getcwd
from os.path import isfile
from ..lib.pwm.pwm_json import JSON_IO
from ..lib.pwm.pwm_system import SystemVersion

# Class Definition


class PWBSConfigFileDontExistError(AssertionError):
    """Error for handling configuration file that don't exist"""
    pass


class PWBSInvalidConfigFile(KeyError):
    """Error for handling invalid configuration file"""
    pass


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
        """Test for existence"""
        self.error = None
        try:
            try:
                assert isfile(self.config_filename_path)
            except AssertionError as e:
                raise PWBSConfigFileDontExistError(
                    "PWBS Configuration File Doesn't Exist!") from e
        except PWBSConfigFileDontExistError as e:
            self.error = e
        """Configuration File Manager"""
        self.filemanager = JSON_IO(self.config_filename_path)
        # Preloading File
        self.load()

    def load(self):
        """Configuration Loader
        Reading JSON from Config File and Converting to Dict.
        """
        self.config_dict = dict(self.filemanager.read())
        try:
            try:
                self.config_dict["commands"]
            except KeyError as e:
                raise PWBSInvalidConfigFile(
                    "PWBS Configuration File is invalid!") from e
        except PWBSInvalidConfigFile as e:
            if self.error is None:
                self.error = e
        return self.config_dict

    def write(self, newdata):
        """Configuration Writer
        Writing JSON to Config File.
        Args:
            newdata: New Data for the Config File.
        """
        return self.filemanager.write(newdata)
