# -*- coding: utf-8 -*-
"""PAiP Web Build System - Test

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
# Imports
# import pytest # @pytest.mark.xfail(raises=AssertionError)
# Documentation
"""
Test 4
================
Tests for v0.4.0dev0 | pwbs.log.logger
================
Test 4.0 - pwbs.log.logger.LoggerAssertionError
Test 4.1 - pwbs.log.logger.BaseLogger
"""
# Test Function


def test_4_0():
    """Testing pwbs.log.logger.LoggerAssertionError"""
    # Import
    from ..logger import LoggerAssertionError
    # Test
    try:
        raise LoggerAssertionError()
        assert False
    except LoggerAssertionError:
        assert True

def test_4_1():
    """Testing pwbs.log.logger.BaseLogger"""
    # Import
    from ..logger import BaseLogger
    # Test
    ## Manual Test in Test
    test_object = BaseLogger()
    print("Test 4.1a | Changing Debug Mode to True..")
    test_object.debug(True)
    assert test_object.debug_state is True
    print("Test 4.1b | Changing Verbose Mode to 255...")
    test_object.verbose(255)
    assert test_object.verbose_state == 255
    test_object.log("Log Method..")
    test_object.log_wop("Log_Wop Method..")
    test_object.log_verbose("Verbose Log Method.._Default")
    test_object.log_verbose("Verbose Log Method.._256",256)
    test_object.log_debug("Debug Log Method..")
    test_object.log_assertion(True, "good assertion")
    test_object.log_assertion(False, "bad assertion")
    