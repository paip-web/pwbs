# -*- coding: utf-8 -*-
"""PAiP Web Build System - Config Manager

This module is Config Manager class for managing everything considered global state of PWBS.

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from typing import Dict
from typing import Any

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Config Manager Class


class ConfigurationNotFoundException(Exception):
    """Exception for when Config Manager don't have registered service name"""
    @staticmethod
    def create_error(config_name: str) -> Exception:
        """
        Create Error Instance for Specified Service Name
        :param str config_name: Service Name
        :return: Error
        """
        return ConfigurationNotFoundException(
            "Configuration {} is not defined".format(config_name)
        )


class ConfigManager:
    """Config Manager Class"""

    """Configuration in Config Manager"""
    config: Dict[str, Any] = {}

    def __init__(self):
        """Service Manager Constructor"""
        self.config = {}

    def __setitem__(self, config_name: str, config: Any):
        """Service Manager Registration"""
        self.config[config_name] = config

    def __contains__(self, config_name: str) -> bool:
        """Config Manager In Configuration Method"""
        return config_name in self.config.keys()

    def __getitem__(self, config_name: str):
        """Service Manager Get Service Method"""
        if config_name in self.config.keys():
            return self.config[config_name]
        raise ConfigurationNotFoundException.create_error(config_name)

    def inject(self, *configuration_to_inject: str, as_kwargs: bool = True):
        """
        Configuration Injector Decorator
        :param configuration_to_inject: Configuration to Inject
        :param as_kwargs: Inject Configuration as kwargs not as configuration object
        """
        def inject(injection_destination):
            """
            Injector Decorator
            :param injection_destination: Decorated Place
            """
            def injector(*args, **kwargs):
                """Injector"""
                configurations = {}
                for configuration in configuration_to_inject:
                    configurations[configuration] = self[configuration]
                if as_kwargs:
                    kwargs = {**kwargs, **configurations}
                else:
                    kwargs['configurations'] = configurations
                return injection_destination(*args, **kwargs)
            return injector
        return inject
