#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Build System

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
### Imports
from datetime import datetime
### Functions and Variables
print_prefix = "PWBS[{0}]: ".format(datetime.now().strftime("%H:%M:%S"))
def print_pref():
    return print_prefix
# TO_TEST: NOT TESTED YET
def verboseSpecific(verbose, level, function, arg=[]):
    if eval(str(verbose)+str(level)):
        return function(*arg)
    else:
        return 0xFF
