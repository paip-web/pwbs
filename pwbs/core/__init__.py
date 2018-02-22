# -*- coding: utf-8 -*-
"""PAiP Web Build System

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from datetime import datetime

# Underscore Variables
__author__ = 'Patryk Adamczyk'
__license__ = 'MIT'
__docformat__ = 'restructuredtext en'

# Globals for PWBS


def prefix_text(text=""):
    """Function to prefix text"""
    return "PWBS[{0}]: {1}".format(datetime.now().strftime("%H:%M:%S"), text)
