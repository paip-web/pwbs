# -*- coding: utf-8 -*-
"""PAiP Web Build System - Service Manager

This module is Service Manager class for managing everything considered global service in PWBS.

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from typing import NewType
from typing import Dict
from typing import Any

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Service Manager Class

ServiceName = NewType('ServiceName', str)
ServiceType = NewType('ServiceType', Any)


class ServiceNotFoundException(Exception):
    """Exception for when Service Manager don't have registered service name"""
    @staticmethod
    def create_error(service_name: ServiceName) -> Exception:
        """
        Create Error Instance for Specified Service Name
        :param ServiceName service_name: Service Name
        :return: Error
        """
        return ServiceNotFoundException(
            "Service {} is not defined".format(service_name)
        )


class ServiceManager:
    """Service Manager Class"""

    """Services registered in Service Manager"""
    services: Dict[ServiceName, ServiceType] = {}

    def __init__(self):
        """Service Manager Constructor"""
        self.services = {}

    def __setitem__(self, service_name: ServiceName, service: ServiceType):
        """Service Manager Registration"""
        self.services[service_name] = service

    def __getitem__(self, service_name: ServiceName):
        """Service Manager Get Service Method"""
        if service_name in self.services.keys():
            return self.services[service_name]
        raise ServiceNotFoundException.create_error(service_name)

    def __contains__(self, service_name: ServiceName):
        """Service Manager Is Service Exist Method"""
        return service_name in self.services.keys()

    def inject(self, *services_to_inject: ServiceName, as_kwargs: bool = True):
        """
        Service Injector Decorator
        :param services_to_inject: Services to Inject
        :param as_kwargs: Inject Services as kwargs not as services object
        """
        def inject(injection_destination):
            """
            Injector Decorator
            :param injection_destination: Decorated Place
            """
            def injector(*args, **kwargs):
                """Injector"""
                services = {}
                for service in services_to_inject:
                    services[service] = self[service]
                if as_kwargs:
                    kwargs = {**kwargs, **services}
                else:
                    kwargs['services'] = services
                return injection_destination(*args, **kwargs)
            return injector
        return inject
