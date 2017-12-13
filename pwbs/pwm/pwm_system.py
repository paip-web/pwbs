#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Module - Reading Informations about system

This module creates function to get information about system.

NAME - PAiP Web Module - OS Information
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
VERSION - v.0.0.0.1
"""
import platform
from collections import namedtuple

def SystemVersion():
    """Printing Debug

    Function to get system information
    Returns:
        namedtuple with information about system
    Return Example:
            machine                 = AMD64
            network_name            = ubuntu
            processor_name          = AMD64 Family 21 Model 48 Stepping 1, AuthenticAMD
            python_compiler         = MSC v.1900 64 bit (AMD64)
            python_implementation   = CPython
            python_version          = 3.6.3
            python_version_tuple    = ('3', '6', '3')
            system_release          = 10
            system_system           = Windows
            system_version          = 10.0.17025
            system_tuple            = ('Windows', '10', '10.0.17025')
            system_uname            = (system='Windows', node='ubuntu', release='10',
                                    version='10.0.17025', machine='AMD64',
                                    processor='AMD64 Family 21 Model 48 Stepping 1, AuthenticAMD')
            platform_info           = ('10', '10.0.17025', 'SP0', 'Multiprocessor Free')
    """
    ver = namedtuple("ver", [
        "machine",
        "network_name",
        "processor_name",
        "python_compiler",
        "python_implementation",
        "python_version",
        "python_version_tuple",
        "system_release",
        "system_system",
        "system_version",
        "system_tuple",
        "system_uname",
        "platform_info"
    ])
    platform_information = ""
    try: # Java Platform
        platform_information = platform.java_ver()
        if platform_information[0] == '':
            raise Exception()
    except Exception:
        try: # Windows Platform
            platform_information = platform.win32_ver()
            if platform_information[0] == '':
                raise Exception()
        except Exception:
            try: # Mac OS Platform
                platform_information = platform.mac_ver()
                if platform_information[0] == '':
                    raise Exception()
            except Exception: # Unknown
                platform_information = ()
    osversion = ver(
        machine=platform.machine(),
        network_name=platform.node(),
        processor_name=platform.processor(),
        python_compiler=platform.python_compiler(),
        python_implementation=platform.python_implementation(),
        python_version=platform.python_version(),
        python_version_tuple=platform.python_version_tuple(),
        system_system=platform.system(),
        system_release=platform.release(),
        system_version=platform.version(),
        system_tuple=platform.system_alias(
            platform.system(),
            platform.release(),
            platform.version()
        ),
        system_uname=platform.uname(),
        platform_info=platform_information
    )
    return osversion
