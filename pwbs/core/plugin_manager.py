# -*- coding: utf-8 -*-
"""PAiP Web Build System - Plugin Manager

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from os import listdir, path
from inspect import getmembers, isclass
from pkgutil import iter_modules
from importlib import import_module
from typing import List
from typing import Union
from pwbs.api.plugin import Plugin

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


# Plugin Manager Class


class PluginManager:
    """Plugin Manager Class"""

    """Plugin Packages To Load"""
    plugin_packages: List[str] = []
    """Loaded Plugins"""
    plugins: List[Plugin] = []
    """Seen Paths in loading"""
    seen_paths: List[str] = []
    """Loaded Plugin Names"""
    plugin_names: List[str] = []

    def __init__(self, plugin_packages: Union[List[str], None] = None):
        """
        Plugin Manager Constructor
        :param plugin_packages: Plugins to Load
        """
        if plugin_packages is None:
            plugin_packages = []
        self.plugin_packages = plugin_packages

    def change_plugins(self, plugins_list: Union[List[str], None] = None) -> None:
        """
        Change, Reload and Initialize Plugins
        :param plugins_list: New List of Plugins to load
        """
        if plugins_list is None:
            plugins_list = []
        self.plugin_packages = plugins_list
        self.reload_plugins()
        self.init_plugins()

    def reload_plugins(self) -> None:
        """Reload Plugins"""
        self.plugins = []
        self.plugin_names = []
        self.seen_paths = []
        plugin_packages = ['pwbs.plugins']
        plugin_packages.extend(self.plugin_packages)
        for plugin_package in plugin_packages:
            self.walk_package(plugin_package)

    def get_loaded_plugin_names(self) -> List[str]:
        """
        Get Loaded Plugin Names
        :return: Loaded Plugin Names
        """
        return self.plugin_names

    def init_plugins(self) -> None:
        """Init all plugins"""
        for plugin in self.plugins:
            plugin.init()

    def walk_package(self, package: str) -> None:
        """
        Walk through Package to find plugins
        :param package: Package Name
        """
        # pylint: disable=too-many-nested-blocks
        try:
            imported_package = import_module(package)
            imported_package_path = imported_package.__path__
            imported_package_name = imported_package.__name__ + '.'
            for _, plugin_name, is_pkg in iter_modules(imported_package_path, imported_package_name):
                if not is_pkg:
                    try:
                        plugin_module = import_module(plugin_name)
                        class_members = getmembers(plugin_module, isclass)
                        for (_, c) in class_members:
                            # Only add classes that are a sub class of Plugin, but NOT Plugin itself
                            if issubclass(c, Plugin) & (c is not Plugin):
                                self.plugins.append(c())
                                self.plugin_names.append("{}::{}".format(plugin_name, c.__name__))
                    except ModuleNotFoundError:
                        pass
            # Now that we have looked at all the modules in the current package, start looking
            # recursively for additional modules in sub packages
            all_current_paths = []
            if isinstance(imported_package.__path__, str):
                all_current_paths.append(imported_package.__path__)
            else:
                all_imported_package_paths = []
                for x in imported_package.__path__:
                    all_imported_package_paths.append(x)
                all_current_paths.extend(all_imported_package_paths)
            for pkg_path in all_current_paths:
                if pkg_path not in self.seen_paths:
                    self.seen_paths.append(pkg_path)
                    # Get all sub directory of the current package path directory
                    child_packages = [p for p in listdir(pkg_path) if path.isdir(path.join(pkg_path, p))]
                    # For each sub directory, apply the walk_package method recursively
                    for child_pkg in child_packages:
                        self.walk_package(package + '.' + child_pkg)
        except ModuleNotFoundError:
            pass
