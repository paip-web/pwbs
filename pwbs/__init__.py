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
__version__ = '0.5.0-dev2'
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Imports

import sentry_sdk
from pwbs.pwbs_class import PWBS
from pwbs.lib.pwm.pwm_system import SystemVersion

# Running as pwbs command


def main():
    """Main Function of Program"""
    sentry_sdk.init(
        "https://0398c7c94f4d4d8fb3e1907598038d71@sentry.io/1452213",
        release=("{0}@{1}".format(__title__, __version__))
    )

    with sentry_sdk.configure_scope() as scope:
        sys_info = SystemVersion()
        scope.set_extra("network_name", sys_info.network_name)
        scope.set_extra(
            "python_version",
            "{0} v{1} compiled with {2}".format(
                sys_info.python_implementation,
                sys_info.python_version,
                sys_info.python_compiler,
            )
        )
        scope.set_extra(
            "os_version",
            "{0} {1}".format(
                sys_info.system_system,
                sys_info.system_version
            )
        )

    pwbs_class_var = PWBS()
    pwbs_class_var.main()


if __name__ == '__main__':
    main()
