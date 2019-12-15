# -*- coding: utf-8 -*-
"""PAiP Web Build System - Test

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
# Documentation
"""
Test 7
================
Tests for v0.6.0dev0 | pwbs.core.plugin_manager
================
Test 7.0 - Load example plugin
Test 7.1 - Try load invalid plugin path
"""
# Test Function


def test_7_0():
    """Load example plugin"""
    # Import
    from pwbs.core.plugin_manager import PluginManager
    # Tests
    pm = PluginManager()
    plugin_name = 'pwbs.tests.test_packages.test_7'
    pm.change_plugins([plugin_name])
    assert len(pm.plugin_packages) == 1
    assert pm.plugin_packages[0] == plugin_name
    assert len(pm.plugins) >= 1
    assert pm.plugins[-1].test == 22


def test_7_1():
    """Try load invalid plugin path"""
    # Import
    from pwbs.core.plugin_manager import PluginManager
    # Tests
    pm = PluginManager()
    plugin_name = 'pwbs.tests.test_packages.test_7.invalid_plugin'
    pm.change_plugins([plugin_name])
    assert len(pm.plugin_packages) == 1
    assert pm.plugin_packages[0] == plugin_name
