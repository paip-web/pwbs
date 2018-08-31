# -*- coding: utf-8 -*-
"""PAiP Web Build System - Singleton Pattern Class

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Singleton Exception
class SingletonException(Exception):
    """This is exception for Singleton Pattern Class"""
    pass


# Singleton Class

class Singleton(object):
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise SingletonException("This class is a singleton!")
        else:
            Singleton.__instance = self
