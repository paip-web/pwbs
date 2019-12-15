# -*- coding: utf-8 -*-
"""PAiP Web Build System - Initialization Plugin

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
import argparse as ap
from gettext import gettext as _
from pwbs.api.plugin import Plugin
from pwbs.core import service_manager
from pwbs.core import event_manager
from pwbs import __version__ as pwbs_version
from pwbs.config.config_manager import PWBSConfigFileDontExistError
from pwbs.config.config_manager import PWBSInvalidConfigFile
from pwbs.config.pwbs_config import PWBS_ConfigManager as PWBS_CM
from pwbs.lib.argparse_plugins import FileNameType

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class InitPlugin(Plugin):
    """Initialization Plugin Class"""

    def init(self):
        """
        Plugin Initialization Method
        """
        pass

    @staticmethod
    @event_manager.handler_decorator('@pwbs/init')
    def initialize_pwbs(*args, nf, **kwargs):
        """Initialize PWBS"""
        service_manager['argument_parser'] = ap.ArgumentParser(
            formatter_class=ap.RawTextHelpFormatter,
            prog="pwbs",
            usage="%(prog)s [Options] Tasks",
            description="PAiP Web Build System v.{0}".format(pwbs_version),
            epilog="Build System based on JSON configuration files.",
            add_help=False,
        )
        event_manager('@pwbs/init/init_argument_parser', *args, **kwargs)
        event_manager('@pwbs/init/init_config', *args, **kwargs)
        event_manager('@pwbs/init/local_config', *args, **kwargs)
        service_manager['config']['arguments'] = None
        service_manager['argument_parser'].add_argument(
            '-h',
            '--help',
            required=False,
            action="store_true",
            help=_('show this help message and exit'),
        )
        service_manager['config']['arguments'] = service_manager['argument_parser'].parse_args()
        service_manager['log'].log_debug("Argument Parser: {0}".format(repr(service_manager['config']['arguments'])))
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/init/init_argument_parser')
    def initialize_argument_parser(*args, nf, **kwargs):
        """Initialize Argument Parser"""
        service_manager['argument_parser/special'] = service_manager['argument_parser'].add_argument_group(
            "Special Tasks",
            "Special Builtin PWBS Functions and Flags")
        service_manager['argument_parser/special'].add_argument(
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
        service_manager['argument_parser/special'].add_argument(
            "--debug",
            default=False,
            action="store_true",
            required=False,
            help="""Changing Debug Mode:
            \nDebug Mode Turned On [Good with -v 255]
            \nDebug Mode Turned Off [Default]""")
        service_manager['argument_parser/special'].add_argument(
            "--version",
            action="store_true",
            required=False,
            help="""Showing Version of PWBS""")
        service_manager['argument_parser/special'].add_argument(
            "--new-config",
            action="store_true",
            required=False,
            help="""Creating Blank Configuration File from basic template""")
        service_manager['argument_parser/special'].add_argument(
            "-l",
            "--log",
            action="store_true",
            required=False,
            help="""Enabling Logging To File""")
        service_manager['argument_parser/special'].add_argument(
            "-lf",
            "--logfile",
            "--log-file",
            required=False,
            type=FileNameType("w"),
            help="""Specifying Log File
            \nDefault Log File: ./pwbs.log""")
        service_manager['argument_parser/special'].add_argument(
            "-c",
            "--configfile",
            "--config-file",
            required=False,
            type=FileNameType("r"),
            help="""Specifying Configuration File
            \nDefault Configuration File: ./pwbs.json""")
        service_manager['argument_parser/special'].add_argument(
            "--test-mode",
            action="store_true",
            required=False,
            help="""Enabling Test Mode
            \nThis option is to use only in tests (automated and manual)""")
        service_manager['argument_parser/special'].add_argument(
            "--run-tests",
            action="store_true",
            required=False,
            help="""Starting PWBS Self-Testing Module""")
        service_manager['argument_parser'].add_argument(
            "Task",
            nargs="*",
            help="""Task""")
        service_manager['argument_parser/local'] = service_manager['argument_parser'].add_argument_group(
            "Local Tasks",
            "Local Configuration Tasks")
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/init/init_config')
    def initialize_config(*args, nf, config='pwbs.json', **kwargs):
        """Initialize Configuration Manager"""
        service_manager['config_manager'] = PWBS_CM(config)
        """Try for errors"""
        if isinstance(
                service_manager['config_manager'].configmanager.error,
                PWBSConfigFileDontExistError,
        ):
            print("Warning: Configuration File Doesn't Exist!")
            service_manager['config_manager'].log.log_debug(
                "CALLER: pwbs.pwbs_class.PWBS.__init__()",
            )
            service_manager['config_manager'].log.log_debug(
                repr(service_manager['config_manager'].configmanager.error),
            )
        elif isinstance(
                service_manager['config_manager'].configmanager.error,
                PWBSInvalidConfigFile,
        ):
            print("Warning: Configuration File is Invalid")
            service_manager['config_manager'].log.log_debug(
                "CALLER: pwbs.pwbs_class.PWBS.__init__()",
            )
            service_manager['config_manager'].log.log_debug(
                repr(service_manager['config_manager'].configmanager.error),
            )
        service_manager['log'] = service_manager['config_manager'].log
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/init/local_config')
    @service_manager.inject('log', 'config_manager')
    @service_manager.inject('argument_parser/local', as_kwargs=False)
    def initialize_local_config(*args, nf, log, config_manager, services, **kwargs):
        """Initialize Local Configuration"""
        try:
            config_manager.commands_to_commandlist()
            for cmd in config_manager.commands.items():
                arg = cmd.argument_parser()
                services['argument_parser/local'].add_argument(cmd.name, nargs="?", help=arg)
        except PWBSConfigFileDontExistError as e:
            log.log_debug("CALLER: pwbs.pwbs_class.PWBS.localconfig_parser_initializer()")
            log.log_debug(repr(e))
        except PWBSInvalidConfigFile as e:
            if isinstance(config_manager.configmanager.error, PWBSConfigFileDontExistError):
                log.log_debug("CALLER: pwbs.pwbs_class.PWBS.localconfig_parser_initializer()")
                log.log_debug(repr(e))
            else:
                print("Warning: Configuration File is Invalid")
                log.log_debug("CALLER: pwbs.pwbs_class.PWBS.localconfig_parser_initializer()")
                log.log_debug(repr(e))
        return nf(*args, **kwargs)
