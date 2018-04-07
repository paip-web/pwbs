# -*- coding: utf-8 -*-
"""PAiP Web Build System - Tests Module
This module contains tests in the submodules.
In exacly this file is some functions for runnning tests from code.
READ - README.md in tests for rules of tests

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
# Global Imports
from datetime import datetime
# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'
# Special Exceptions


class TestSucceed(Exception):
    """Exception For Passed Test"""
    pass


class TestFailed(Exception):
    """Exception For Failed Test"""
    pass

# Special Functions


def tests_prefix_text(text=""):
    """Function to prefix text [Test Runner Version]
    Default Prefixer
    Args:
        text (:obj:`str`): Text to prefix
    """
    return print("PWBS_TEST[{0}]: {1}".format(
        datetime.now().strftime("%H:%M:%S"),
        text))


def run_test(
        test_function,
        test_name: str,
        test_comment: str,
        test_module: str,
        test_except_to_fail=False):
    tests_prefix_text(
        "Testing {0} in Test {1}".format(
            test_module,
            test_name))
    tests_prefix_text(
        "Comment for Test {0}: {1}".format(
            test_name,
            test_comment))
    try:
        try:
            test_function()
            raise TestSucceed(test_name)
        except AssertionError as e:
            if test_except_to_fail:
                raise TestSucceed(test_name) from e
            raise TestFailed(test_name) from e
    except TestSucceed:
        tests_prefix_text(
            "[RESPONSE]: Test {0} - Success!".format(
                test_name))
    except TestFailed:
        tests_prefix_text(
            "[RESPONSE]: Test {0} - Fail!".format(
                test_name))


def test_runner():
    # ################## Test 0
    from .test_0 import test_0_0, test_0_1
    # # Test 0.0
    run_test(test_0_0,
             "0.0",
             "Test Asserting True",
             "Python",
             False)
    # # Test 0.0
    run_test(test_0_1,
             "0.1",
             "Test Asserting False",
             "Python",
             True)
    # ################## Test 1
    from .test_1 import test_1_0, test_1_1, test_1_2, test_1_3
    from .test_1 import test_1_4, test_1_5, test_1_6
    from .test_1 import test_1_7, test_1_8, test_1_9
    # # Test 1.0
    run_test(test_1_0,
             "1.0",
             "Testing Values",
             "pwbs.command.command.CommandType",
             False)
    # # Test 1.1
    run_test(test_1_1,
             "1.1",
             "Testing Values",
             "pwbs.command.command.Platform",
             False)
    # # Test 1.2
    run_test(test_1_2,
             "1.2",
             "Testing Values",
             "pwbs.command.command.CommandMode",
             False)
    # # Test 1.3
    run_test(test_1_3,
             "1.3",
             "Test Command",
             "pwbs.command.command.Command",
             False)
    # # Test 1.4
    run_test(test_1_4,
             "1.4",
             "Test Command",
             "pwbs.command.command.Command",
             False)
    # # Test 1.5
    run_test(test_1_5,
             "1.5",
             "Test Command",
             "pwbs.command.command.Command",
             False)
    # # Test 1.6
    run_test(test_1_6,
             "1.6",
             "Test Command",
             "pwbs.command.command.Command",
             False)
    # # Test 1.7
    run_test(test_1_7,
             "1.7",
             "Test Command",
             "pwbs.command.command.Command",
             False)
    # # Test 1.8
    run_test(test_1_8,
             "1.8",
             "Test Command",
             "pwbs.command.command.Command",
             False)
    # # Test 1.9
    run_test(test_1_9,
             "1.9",
             "Test CommandList",
             "pwbs.command.command.CommandList",
             False)
