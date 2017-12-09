#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Build System

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
### Underscore Variables
__title__ = 'pwbs'
__version__ = '0.0.1-dev3'
__author__ = 'Patryk Adamczyk'
__license__ = 'MIT'
__docformat__ = 'restructuredtext en'
### Imports
import sys
from os import path, getcwd
### Imports from package
from .pwbs import baner
### Functions
def main(args=sys.argv):
    """Główna Funkcja Programu"""
    '''verbose_mode:
    0 - No Verbose
    1 - Small Verbose [Default] | Baner / Better Task View
    2 - Medium Verbose | Bigger Banner / Small Verbose Task View
    3 - Full Verbose | Logging to console more things
    255 - Extreme Verbose | Logging everything to console
    '''
    verbose_mode = 3 #Dev Version Thing
    cwd = getcwd()
    script_cwd = path.abspath(path.dirname(__file__))
    baner(__version__, verbose_mode, args)
    sys.exit()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
