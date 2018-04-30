# -*- coding: utf-8 -*-
"""PAiP Web Build System - Test

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
# Documentation
"""
Test 3
================
Tests for v0.4.0dev0 | pwbs.config
================
Test 3.0 - pwbs.core.NotImplementedFeatureError
Test 3.1 - pwbs.core.prefix_text | TO_TEST: BAD TEST - Temporary Solution
"""
# Test Function


def test_3_0():
    """Testing pwbs.core.NotImplementedFeatureError"""
    # Import
    from ..core import NotImplementedFeatureError
    # Test
    try:
        raise NotImplementedFeatureError()
        assert False
    except NotImplementedFeatureError:
        assert True

def test_3_1():
    """Testing pwbs.core.prefix_text"""
    # Import
    from ..core import prefix_text
    from datetime import datetime
    # Values
    assert prefix_text(10) == "PWBS[{0}]: {1}".format(datetime.now().strftime("%H:%M:%S"), 10)
