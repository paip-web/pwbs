# -*- coding: utf-8 -*-
"""PAiP Web Build System - Special Task Interpreter Plugin

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
"""
# Imports
from pwbs.api.plugin import Plugin
from pwbs.core import service_manager
from pwbs.core import event_manager
from pwbs.core import config_manager
from pwbs import __version__ as pwbs_version
from pwbs.tests import test_runner

# Underscore Variables
"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


class SpecialPlugin(Plugin):
    """Special Task Interpreter Plugin Class"""

    def init(self):
        """
        Plugin Initialization Method
        """
        pass

    @staticmethod
    @event_manager.handler_decorator('@pwbs/interpreter/special')
    @service_manager.inject('log')
    @config_manager.inject('arguments')
    def verbose(*args, nf, log, arguments, **kwargs):
        """Set Verbose Level"""
        log.verbose(int(arguments.verbose))
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/interpreter/special')
    @service_manager.inject('log')
    @config_manager.inject('arguments')
    def debug(*args, nf, log, arguments, **kwargs):
        """Set Debug Mode"""
        log.debug(arguments.debug)
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/interpreter/special')
    @service_manager.inject('log')
    @config_manager.inject('arguments')
    def test_mode(*args, nf, log, arguments, **kwargs):
        """Test Mode"""
        if arguments.test_mode is True:
            log.debug(True)
            log.verbose(255)
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/interpreter/special')
    @config_manager.inject('arguments')
    def version(*args, nf, arguments, executed=False, **kwargs):
        """Version"""
        if arguments.version is True:
            print("PAiP Web Build System v.{0}".format(pwbs_version))
            return nf(*args, executed=True, **kwargs)
        return nf(*args, executed, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/interpreter/special')
    @config_manager.inject('arguments')
    @service_manager.inject('log')
    def logfile(*args, nf, arguments, log, **kwargs):
        """Initialize"""
        if arguments.logfile is not None:
            log.log_logger.logfile = arguments.logfile
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/interpreter/special')
    @config_manager.inject('arguments')
    @service_manager.inject('log')
    def log(*args, nf, arguments, log, **kwargs):
        """Active Logging"""
        if arguments.log is True:
            log.log_logger.activelogging = True
            log.log_file_write()
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/interpreter/special')
    @config_manager.inject('arguments')
    def config_file(*args, nf, arguments, **kwargs):
        """Set Configuration File"""
        if arguments.configfile is not None:
            kwargs_extended = {'config': arguments.configfile}
            kwarg = {**kwargs, **kwargs_extended}
            kwarg = dict(kwarg)
            event_manager('@pwbs/init', *args, **kwarg)
        return nf(*args, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@pwbs/interpreter/special')
    @config_manager.inject('arguments')
    def run_tests(*args, nf, arguments, executed=False, **kwargs):
        """Run Tests"""
        if arguments.run_tests is True:
            test_runner()
            return nf(*args, executed=True, **kwargs)
        return nf(*args, executed, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@after_@pwbs/interpreter/special')
    @service_manager.inject('argument_parser')
    @config_manager.inject('arguments')
    def print_help(*args, nf, arguments, argument_parser, executed=False, **kwargs):
        """Print Help Message"""
        if (arguments.help is not None and arguments.help is True) or ((len(arguments.Task) == 0) and (not executed)):
            argument_parser.print_help()
            return nf(*args, executed=True, **kwargs)
        return nf(*args, executed, **kwargs)

    @staticmethod
    @event_manager.handler_decorator('@after_@pwbs/interpreter/special')
    def is_executed(*args, nf, executed=False, **kwargs):
        """Set Verbose Level"""
        return executed
