# -*- coding: utf-8 -*-
"""PAiP Web Build System - Program Class
This module contains the most core functionality,
needed by other functions and classes.

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
import argparse as ap
from . import __version__ as pwbs_version

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Main Program Class


class PWBS(object):
    """PAiP Web Build System - Program Class"""
    def __init__(self):
        """Constructor of the Main Program Class"""
        """Argument Parser"""
        self.argparser = ap.ArgumentParser(
            prog="pwbs",
            usage="%(prog)s [Options] Tasks",
            description="PAiP Web Build System v.{0}".format(pwbs_version),
            epilog="Build System based on JSON configuration files.")
        self.parser_initializer()

    def parser_initializer(self):
        self.argparser_specialtasks = self.argparser.add_argument_group(
            "Special Tasks")
        self.argparser_specialtasks.add_argument(
            "-v",
            "--verbose",
            default=1,
            type=int,
            choices=[0, 1, 2, 3, 255],
            required=False,
            help="""Changing Verbosity:
            \n0 - No Information about running
            \n1 - Normal Information about running [Default]
            \n2 - More Information about running
            \n3 - Much Information about running and work behind the scenes
            \n255 - Debug Verbosity Mode""")
        self.argparser_specialtasks.add_argument(
            "--debug",
            default=False,
            type=bool,
            required=False,
            help="""Changing Debug Mode:
            \nTrue - Debug Mode Turned On [Good with -v 255]
            \nFalse - Debug Mode Turned Off [Default]""")
        self.argparser_specialtasks.add_argument(
            "--version",
            action="store_true",
            type=bool,
            required=False,
            help="""Showing Version of PWBS""")
        self.argparser_specialtasks.add_argument(
            "--new-config",
            action="store_true",
            type=bool,
            required=False,
            help="""Creating Blank Configuration File from basic template""")
        self.argparser_specialtasks.add_argument(
            "-l",
            "--log",
            action="store_true",
            required=False,
            help="""Enabling Logging To File""")
        self.argparser_specialtasks.add_argument(
            "-lf",
            "--logfile",
            "--log-file",
            required=False,
            type=ap.FileType("w"),
            help="""Specifying Log File
            \nDefault Log File: ./pwbs.log""")
        self.argparser_specialtasks.add_argument(
            "-c",
            "--configfile",
            "--config-file",
            required=False,
            type=ap.FileType("rw"),
            help="""Specifying Configuration File
            \nDefault Configuration File: ./pwbs.json""")
        self.argparser_specialtasks.add_argument(
            "--test-mode",
            action="store_true",
            required=False,
            type=bool,
            help="""Enabling Test Mode
            \nThis option is to use only in tests (automated and manual)""")
        self.argparser_specialtasks.add_argument(
            "--run-tests",
            action="store_true",
            required=False,
            type=bool,
            help="""Starting PWBS Self-Testing Module""")
