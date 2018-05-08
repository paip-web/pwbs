# -*- coding: utf-8 -*-
"""PAiP Web Build System - Test

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
# Documentation
"""
Test 5
================
Tests for v0.4.0dev0 | pwbs.log.logger
================
Test 5.0 - pwbs.log.logger.LoggerAssertionError
Test 5.1 - pwbs.log.logger.BaseLogger
Test 5.2 - pwbs.log.logger.LogLogger
Test 5.3 - pwbs.log.logger.Logger
# Test 5.2,5.3 not covered test_object.log_file_write()
"""
# Test Function


def test_5_0():
    """Testing pwbs.log.logger.LoggerAssertionError"""
    # Import
    from ..log.logger import LoggerAssertionError
    # Tests
    try:
        raise LoggerAssertionError()
        assert False
    except LoggerAssertionError:
        assert True


def test_5_1():
    """Testing pwbs.log.logger.BaseLogger"""
    # Import
    from ..log.logger import BaseLogger, LoggerAssertionError
    # Tests
    test_object = BaseLogger()
    # # Debug
    test_object.log_debug("Test 5.1.1 - You shouldn't see that text immidiately")
    test_object.debug(True)
    test_object.log_debug("Test 5.1.1 - You should see that text immidiately")
    # # Verbose
    test_object.log_verbose("Test 5.1.2 - You shouldn't see that text")
    test_object.verbose(255)
    test_object.log_verbose("Test 5.1.2 - You should see that text")
    # # Log Methods and Variations
    test_object.log("Test 5.1.3 - Log Method")
    test_object.log_wop("Test 5.1.3 - Log Without Prefixer Method")
    test_object.log_assertion(True, "Test 5.1.3 - Assertion")
    try:
        test_object.log_assertion(False, "Test 5.1.3 - Assertion")
        raise NotImplementedError()
    except LoggerAssertionError:
        assert True


def test_5_2():
    """Testing pwbs.log.logger.LogLogger"""
    # Import
    from ..log.logger import LogLogger, LoggerAssertionError
    # Tests
    test_object = LogLogger()
    test_array = test_object.story
    # # Debug
    test_object.log_debug("Test 5.2.1 - You shouldn't see that text immidiately")
    if test_array == test_object.story:
        assert False
    if not(test_object.debug_state is False):
        assert False
    test_object.debug(True)
    if not(test_object.debug_state is True):
        assert False
    test_object.log_debug("Test 5.2.1 - You should see that text immidiately")
    if not(test_array == test_object.story):
        assert False
    test_array = test_object.story
    # # Verbose
    test_object.log_verbose("Test 5.2.2 - You shouldn't see that text")
    if test_array == test_object.story:
        assert False
    test_array = test_object.story
    if not(test_object.verbose_state == 1):
        assert False
    test_object.verbose(255)
    if not(test_object.verbose_state == 255):
        assert False
    test_object.log_verbose("Test 5.2.2 - You should see that text")
    if not(test_array == test_object.story):
        assert False
    test_array = test_object.story
    # # Log Methods and Variations
    test_object.log("Test 5.2.3 - Log Method")
    if not(test_array == test_object.story):
        assert False
    test_array = test_object.story
    test_object.log_wop("Test 5.2.3 - Log Without Prefixer Method")
    if not(test_array == test_object.story):
        assert False
    test_array = test_object.story
    test_object.log_assertion(True, "Test 5.2.3 - Assertion")
    if not(test_array == test_object.story):
        assert False
    test_array = test_object.story
    try:
        test_object.log_assertion(False, "Test 5.2.3 - Assertion")
        if not(test_array == test_object.story):
            assert False
        test_array = test_object.story
        raise NotImplementedError()
    except LoggerAssertionError:
        assert True


def test_5_3():
    """Testing pwbs.log.logger.Logger"""
    # Import
    from ..log.logger import Logger, LoggerAssertionError
    # Tests
    test_object = Logger()
    # # # BaseLogger Part
    # # Debug
    test_object.log_debug("Test 5.3.1 - You shouldn't see that text immidiately")
    test_object.debug(True)
    test_object.log_debug("Test 5.3.1 - You should see that text immidiately")
    # # Verbose
    test_object.log_verbose("Test 5.3.2 - You shouldn't see that text")
    test_object.verbose(255)
    test_object.log_verbose("Test 5.3.2 - You should see that text")
    # # Log Methods and Variations
    test_object.log("Test 5.3.3 - Log Method")
    test_object.log_wop("Test 5.3.3 - Log Without Prefixer Method")
    test_object.log_assertion(True, "Test 5.3.3 - Assertion")
    try:
        test_object.log_assertion(False, "Test 5.3.3 - Assertion")
        raise NotImplementedError()
    except LoggerAssertionError:
        assert True
    # # # LogLogger Part
    # # Debug
    test_object.log_debug("Test 5.3.4 - You shouldn't see that text immidiately")
    if test_array == test_object.story():
        assert False
    if not(test_object.debug_state is False):
        assert False
    test_object.debug(True)
    if not(test_object.debug_state is True):
        assert False
    test_object.log_debug("Test 5.3.4 - You should see that text immidiately")
    if not(test_array == test_object.story()):
        assert False
    test_array = test_object.story()
    # # Verbose
    test_object.log_verbose("Test 5.3.5 - You shouldn't see that text")
    if test_array == test_object.story():
        assert False
    test_array = test_object.story()
    if not(test_object.verbose_state == 1):
        assert False
    test_object.verbose(255)
    if not(test_object.verbose_state == 255):
        assert False
    test_object.log_verbose("Test 5.3.5 - You should see that text")
    if not(test_array == test_object.story()):
        assert False
    test_array = test_object.story()
    # # Log Methods and Variations
    test_object.log("Test 5.3.6 - Log Method")
    if not(test_array == test_object.story()):
        assert False
    test_array = test_object.story()
    test_object.log_wop("Test 5.3.6 - Log Without Prefixer Method")
    if not(test_array == test_object.story()):
        assert False
    test_array = test_object.story()
    test_object.log_assertion(True, "Test 5.3.6 - Assertion")
    if not(test_array == test_object.story()):
        assert False
    test_array = test_object.story()
    try:
        test_object.log_assertion(False, "Test 5.3.6 - Assertion")
        if not(test_array == test_object.story()):
            assert False
        test_array = test_object.story()
        raise NotImplementedError()
    except LoggerAssertionError:
        assert True
