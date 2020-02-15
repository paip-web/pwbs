# -*- coding: utf-8 -*-
"""PAiP Web Build System - Initialization Plugin

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT
"""
# Imports
import argparse as ap
from gettext import gettext as _
from pwbs.api.plugin import Plugin
from pwbs.core import service_manager
from pwbs.core import event_manager
from pwbs.core import config_manager
from pwbs import __version__ as pwbs_version
from pwbs.config.config_manager import PWBSConfigFileDontExistError
from pwbs.config.config_manager import PWBSInvalidConfigFile
from pwbs.lib.argparse_plugins import FileNameType
from pwbs.log.logger import Logger
from pwbs.config.config_manager import ConfigManager
from pwbs.tasks.task_factory import TaskFactory

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
        service_manager['log'] = Logger() if 'log' not in service_manager.services.keys() else service_manager['log']
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
        service_manager['argument_parser'].add_argument(
            '--run-inside-docker',
            required=False,
            dest="run_in_docker",
            action="store_true",
            help="""Run specified tasks in docker container
            \nThis flag does not work in a Docker Container""",
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
        service_manager['argument_parser/task-options'] = service_manager['argument_parser'].add_argument_group(
            "Tasks Options",
            "Task Options Flags that provide additional data to task commands")
        service_manager['argument_parser/task-options'].add_argument(
            '-fa',
            '--forward-args',
            '--forward-arguments',
            required=False,
            dest="arguments_to_forward",
            nargs=ap.REMAINDER,
            help="""Provide arguments you want to be provided to all of your commands in tasks
            \nThis flag cannot be used with --args flag""",
        )
        service_manager['argument_parser/task-options'].add_argument(
            '-a',
            '--args',
            required=False,
            dest="arguments_for_tasks",
            nargs=ap.REMAINDER,
            help="""Provide arguments accessible in task commands
            \nThis flag cannot be used with --forward-arguments flag""",
        )
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
        service_manager['config_manager'] = ConfigManager(config)
        service_manager['log'].log_debug("Loading Configuration File Data...")
        commands = service_manager['config_manager'].load()
        config_manager['config_data'] = commands
        service_manager['log'].log_debug("Configuration File Data Loaded.")
        """Try for errors"""
        if isinstance(service_manager['config_manager'].error, PWBSConfigFileDontExistError):
            print("Warning: Configuration File Doesn't Exist!")
            service_manager['log'].log_debug(repr(service_manager['config_manager'].error))
        elif isinstance(service_manager['config_manager'].error, PWBSInvalidConfigFile):
            print("Warning: Configuration File is Invalid")
            service_manager['log'].log_debug(repr(service_manager['config_manager'].error))
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/init/local_config')
    @service_manager.inject('log')
    @service_manager.inject('argument_parser/local', 'config_manager', as_kwargs=False)
    def initialize_local_config(*args, nf, log, services, **kwargs):
        """Initialize Local Configuration"""
        try:
            config_manager['tasks'] = TaskFactory.make_list(config_manager['config_data'].get('commands', {}))
            for task in config_manager['tasks'].items():
                services['argument_parser/local'].add_argument(task.name, nargs="?", help=task.comment)
        except PWBSConfigFileDontExistError as e:
            log.log_debug(repr(e))
        except PWBSInvalidConfigFile as e:
            if isinstance(services['config_manager'].configmanager.error, PWBSConfigFileDontExistError):
                log.log_debug(repr(e))
            else:
                print("Warning: Configuration File is Invalid")
                log.log_debug(repr(e))
        return nf(*args, **kwargs)
