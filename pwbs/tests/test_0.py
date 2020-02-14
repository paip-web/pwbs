# -*- coding: utf-8 -*-
"""PAiP Web Build System - Test

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
import pytest
# Documentation
"""
Test 0
================
Test for test
"""
# Test Function


def test_0_0():
    assert True


@pytest.mark.xfail(raises=AssertionError)
def test_0_1():
    assert False
