# -*- coding: utf-8 -*-
"""PAiP Web Build System - Tests Module
This module contains tests in the submodules.
In exacly this file is some functions for runnning tests from code.

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


class TestSucceed(AssertionError):
    """Exception For Passed Test"""
    pass


class TestFailed(AssertionError):
    """Exception For Failed Test"""
    pass

# Special Functions


def tests_prefix_text(text=""):
    """Function to prefix text [Test Runner Version]
    Default Prefixer
    Args:
        text (:obj:`str`): Text to prefix
    """
    return "PWBS_TEST[{0}]: {1}".format(
        datetime.now().strftime("%H:%M:%S"),
        text)


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
    from test_0 import test_0_0, test_0_1
    # # Test 0.0
    run_test(test_0_0, "0.0", "Test Asserting True", "Python", False)
    # # Test 0.0
    run_test(test_0_1, "0.1", "Test Asserting False", "Python", True)
