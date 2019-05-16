# -*- coding: utf-8 -*-
"""PAiP Web Build System - Test

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
# Documentation
"""
Test 2
================
Tests for v0.4.0dev0 | pwbs.config
================
Test 2.0 - 2.1 - pwbs.config.config_manager.*
# Test 2.0 - Exceptions Tests
# Test 2.1 - Config Manager Tests
# Test 2.2 - pwbs.config.pwbs_config.PWBS_ConfigManager
"""
# Test Function


def test_2_0():
    """Testing Exceptions"""
    # Import
    from ..config.config_manager import PWBSConfigFileDontExistError
    from ..config.config_manager import PWBSInvalidConfigFile
    # Test
    try:
        raise PWBSConfigFileDontExistError()
        assert False
    except PWBSConfigFileDontExistError:
        assert True
    try:
        raise PWBSInvalidConfigFile()
        assert False
    except PWBSInvalidConfigFile:
        assert True

def test_2_1():
    """Testing Config Manager"""
    # Import
    from ..config.config_manager import ConfigManager
    from ..config.config_manager import PWBSConfigFileDontExistError
    from ..config.config_manager import PWBSInvalidConfigFile
    # Values
    try:
        t1 = ConfigManager("pwbs.test.json")
        t1.write(t1.load())
    except PWBSConfigFileDontExistError:
        assert True # It's Working
    except PWBSInvalidConfigFile:
        assert True # It's Working


def test_2_2():
    """Testing PWBS Config Manager"""
    # Import
    from ..config.pwbs_config import PWBS_ConfigManager
    from ..config.config_manager import PWBSConfigFileDontExistError
    from ..config.config_manager import PWBSInvalidConfigFile
    # Values
    t1 = PWBS_ConfigManager()
    t1.log.log("Test 2.2")
    try:
        t1.config_file()
        t1.commands_to_commandlist()
    except PWBSConfigFileDontExistError:
        assert True # It's Working
    except PWBSInvalidConfigFile:
        assert True # It's Working
