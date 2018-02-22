#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Build System

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
### Underscore Variables
__name__ = 'pwbs'
__title__ = 'pwbs'
__version__ = '0.3.0-dev1'
__author__ = 'Patryk Adamczyk'
__license__ = 'MIT'
__docformat__ = 'restructuredtext en'
### Imports
import sys
from os import path, getcwd
### Imports from package
from .pwbs import baner
from .command_interpreter import command_interpreter
### Functions
# TO_TEST: NOT TESTED YET
def main(args=sys.argv):
    """Główna Funkcja Programu"""
    verbose_mode = 3 #DEV: Version Thing
    cwd = getcwd()
    script_cwd = path.abspath(path.dirname(__file__))
    baner(__version__, verbose_mode, args)
    command_interpreter(args[1:], verbose_mode)
    sys.exit()

if __name__ == '__main__':# or __name__ == 'pwbs':
    sys.exit(main(sys.argv))
