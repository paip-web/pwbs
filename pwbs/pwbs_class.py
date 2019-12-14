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
from pwbs import __version__ as pwbs_version
from pwbs.config.config_manager import PWBSConfigFileDontExistError
from pwbs.config.config_manager import PWBSInvalidConfigFile
from pwbs.config.config_manager import ConfigManager
from pwbs.config.pwbs_config import PWBS_ConfigManager as PWBS_CM
from pwbs.core import NotImplementedFeatureError
from pwbs.tests import test_runner
from pwbs.lib.argparse_plugins import FileNameType

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
        """Try for errors"""
        if isinstance(self.pwbscm.configmanager.error, PWBSConfigFileDontExistError):
            print(
                "Warning: Configuration File Doesn't Exist!")
            self.pwbscm.log.log_debug(
                "CALLER: pwbs.pwbs_class.PWBS.__init__()")
            self.pwbscm.log.log_debug(repr(self.pwbscm.configmanager.error))
        elif isinstance(self.pwbscm.configmanager.error, PWBSInvalidConfigFile):
            print(
                "Warning: Configuration File is Invalid")
            self.pwbscm.log.log_debug(
                "CALLER: pwbs.pwbs_class.PWBS.__init__()")
            self.pwbscm.log.log_debug(repr(self.pwbscm.configmanager.error))
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
            action="store_true",
            required=False,
            help="""Changing Debug Mode:
            \nDebug Mode Turned On [Good with -v 255]
            \nDebug Mode Turned Off [Default]""")
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
            type=FileNameType("w"),
            help="""Specifying Log File
            \nDefault Log File: ./pwbs.log""")
        self.argparser_specialtasks.add_argument(
            "-c",
            "--configfile",
            "--config-file",
            required=False,
            type=FileNameType("r"),
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
        self.argparser.add_argument(
            "Task",
            nargs="*",
            help="""Task""")
        self.argparser_localconfigtasks = self.argparser.add_argument_group(
            "Local Tasks",
            "Local Configuration Tasks")

    def localconfig_parser_initializer(self):
        """Local Configuration Parser Initializer"""
        try:
            self.pwbscm.commands_to_commandlist()
            for cmd in self.pwbscm.commands.items():
                arg = cmd.argument_parser()
                self.argparser_localconfigtasks.add_argument(cmd.name, nargs="?", help=arg)
        except PWBSConfigFileDontExistError as e:
            self.pwbscm.log.log_debug("CALLER: pwbs.pwbs_class.PWBS.localconfig_parser_initializer()")
            self.pwbscm.log.log_debug(repr(e))
        except PWBSInvalidConfigFile as e:
            if isinstance(self.pwbscm.configmanager.error,PWBSConfigFileDontExistError):
                self.pwbscm.log.log_debug("CALLER: pwbs.pwbs_class.PWBS.localconfig_parser_initializer()")
                self.pwbscm.log.log_debug(repr(e))
            else:
                print("Warning: Configuration File is Invalid")
                self.pwbscm.log.log_debug("CALLER: pwbs.pwbs_class.PWBS.localconfig_parser_initializer()")
                self.pwbscm.log.log_debug(repr(e))

    def special_tasks_interpreter(self):
        """Special Tasks Interpreter"""
        special_task_executed = False
        self.pwbscm.log.verbose(int(self.args.verbose))
        self.pwbscm.log.debug(self.args.debug)
        if self.args.version is True:
            print("PAiP Web Build System v.{0}".format(pwbs_version))
            special_task_executed = True
        if self.args.log is True:
            self.pwbscm.log.log_logger.activelogging = True
            self.pwbscm.log.log_file_write()
            special_task_executed = True
        if self.args.logfile is not None:
            self.pwbscm.log.log_logger.logfile = self.args.logfile
            special_task_executed = True
        if self.args.configfile is not None:
            self.pwbscm.config_manager = ConfigManager(self.args.configfile)
            self.localconfig_parser_initializer()
            special_task_executed = True
        if self.args.test_mode is True:
            self.pwbscm.log.debug(True)
            self.pwbscm.log.verbose(255)
            special_task_executed = True
        if self.args.run_tests is True:
            print("Test Runner Mode Activated!")
            test_runner()
            special_task_executed = True
        return special_task_executed

    def task_runner(self):
        """Task Runner"""
        for arg in self.args.Task:
            self.pwbscm.commands[arg].run()

    def main(self):
        """Main Function of the Program"""
        try:
            self.args = self.argparser.parse_args()
            self.pwbscm.log.log_debug("Argument Parser: {0}".format(repr(self.args)))
            special_task_executed = self.special_tasks_interpreter()
            self.task_runner()
            if (len(self.args.Task) == 0) and (not special_task_executed):
                self.argparser.print_help()

        except NotImplementedFeatureError as e:
            print("Not Implemented Feature Called!")
