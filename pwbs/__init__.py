# -*- coding: utf-8 -*-
"""PAiP Web Build System

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Underscore Variables

"""Title of Program"""
__title__ = 'pwbs'
"""Version of Program"""
__version__ = '0.5.0-dev0'
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Imports

from .pwbs_class import PWBS
from .api.pwbs_event_manager import PWBSEventManager

# Running as pwbs command

def main():
    """Main Function of Program"""
    # Initialize PWBS Event Manager
    PWBS_EM = PWBSEventManager.initialize()
    pwbs_class_var = PWBS()
    PWBS_EM.startEvent(
        "pwbs-event--pwbs_class-initialized",
        pwbs_var=pwbs_class_var
    )
    PWBS_EM.startEvent(
        "pwbs-event--pwbs_class-before-main",
        pwbs_var=pwbs_class_var
    )
    pwbs_class_var.main()
    PWBS_EM.startEvent(
        "pwbs-event--pwbs_class-after-main",
        pwbs_var=pwbs_class_var
    )


if __name__ == '__main__':
    main()
