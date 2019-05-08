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

import sentry_sdk
from pwbs.pwbs_class import PWBS
from pwbs.api.pwbs_event_manager import PWBSEventManager


# Running as pwbs command


def main():
    """Main Function of Program"""
    sentry_sdk.init(
        "https://0398c7c94f4d4d8fb3e1907598038d71@sentry.io/1452213",
        release=("{0}@{1}".format(__title__, __version__))
    )
    # Initialize PWBS Event Manager
    pwbs_em = PWBSEventManager.initialize()
    pwbs_class_var = PWBS()
    pwbs_em.startEvent(
        "pwbs-event--pwbs_class-initialized",
        pwbs_var=pwbs_class_var
    )
    pwbs_em.startEvent(
        "pwbs-event--pwbs_class-before-main",
        pwbs_var=pwbs_class_var
    )
    pwbs_class_var.main()
    pwbs_em.startEvent(
        "pwbs-event--pwbs_class-after-main",
        pwbs_var=pwbs_class_var
    )


if __name__ == '__main__':
    main()
