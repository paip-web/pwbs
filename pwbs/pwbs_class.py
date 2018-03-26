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
from os import path
from . import __version__ as pwbs_version
from .config.pwbs_config import PWBS_ConfigManager as PWBS_CM
from .lib.pwm.pwm_system import SystemVersion

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
            formatter_class=ap.RawTextHelpFormatter,
            prog="pwbs",
            usage="%(prog)s [Options] Tasks",
            description="PAiP Web Build System v.{0}".format(pwbs_version),
            epilog="Build System based on JSON configuration files.")
        self.parser_initializer()
        """PWBS Config Manager"""
        self.pwbscm = PWBS_CM()
        self.localconfig_parser_initializer()
        """Arguments returned from argparse.parse_args()"""
        self.args = None

    def parser_initializer(self):
        """Parser Initializer"""
        self.argparser_specialtasks = self.argparser.add_argument_group(
            "Special Tasks",
            "Special Bultin PWBS Functions and Flags")
        self.argparser_specialtasks.add_argument(
            "-v",
            "--verbose",
            default="1",
            choices=["0", "1", "2", "3", "255"],
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
            required=False,
            help="""Changing Debug Mode:
            \nTrue - Debug Mode Turned On [Good with -v 255]
            \nFalse - Debug Mode Turned Off [Default]""")
        self.argparser_specialtasks.add_argument(
            "--version",
            action="store_true",
            required=False,
            help="""Showing Version of PWBS""")
        self.argparser_specialtasks.add_argument(
            "--new-config",
            action="store_true",
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
            help="""Enabling Test Mode
            \nThis option is to use only in tests (automated and manual)""")
        self.argparser_specialtasks.add_argument(
            "--run-tests",
            action="store_true",
            required=False,
            help="""Starting PWBS Self-Testing Module""")
        self.argparser_localconfigtasks = self.argparser.add_argument_group(
            "Local Tasks",
            "Local Configuration Tasks")

    def localconfig_parser_initializer(self):
        """Local Configuration Parser Initializer"""
        self.pwbscm.commands_to_commandlist()
        for cmd in self.pwbscm.commands.items():
            arg = cmd.argument_parser()
            self.argparser_localconfigtasks.add_argument(
                cmd.name,
                **arg)

    def special_tasks_interpreter(self):
        """Special Tasks Interpreter"""
        self.pwbscm.log.verbose(int(self.args.verbose))
        self.pwbscm.log.debug(self.args.debug)
        if self.args.version is True:
            print("PAiP Web Build System v.{0}".format(pwbs_version))

    def main(self):
        """Main Function of the Program"""
        self.args = self.argparser.parse_args()
        self.special_tasks_interpreter()
        print(self.args)
