# -*- coding: utf-8 -*-
"""PAiP Web Build System - Event Manager

This module is PWBS Event Manager singleton class for evented programming in PWBS.

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports

from ..lib.singleton import SingletonException

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Event Manager Class

class PWBSEventManager(object):
    """PWBS Event Manager Class"""
    def createEvent(self, name, handlers=None):
        """Create Event"""
        if handlers is None:
            handlers = list()
        self.events[name] = handlers

    def addHandler(self, name, function):
        """Add Handler"""
        self.events[name].append(function)

    def deleteEvent(self, name):
        """Delete Handler"""
        del self.events[name]

    def startEvent(self, event_name, event_name_included=True, **args):
        """Start Event"""
        for f in self.events[event_name]:
            if event_name_included is False:
                f(**args)
            else:
                f(event_name, **args)

    # Event Manager Replacement in Singleton
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if PWBSEventManager.__instance is None:
            PWBSEventManager()
        return PWBSEventManager.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if PWBSEventManager.__instance is not None:
            raise SingletonException("This class is a singleton!")
        else:
            PWBSEventManager.__instance = self
        self.events = {}

    @staticmethod
    def initialize():
        """This function initializes Event Manager for use in PWBS"""
        # PWBS Event Manager
        PWBS_EM = PWBSEventManager()
        # PWBS Event Called in pwbs.__init__.main() when PWBS class is initialized
        PWBS_EM.createEvent("pwbs-event--pwbs_class-initialized")
        # PWBS Event Called in pwbs.__init__.main() before PWBS.main() is called
        PWBS_EM.createEvent("pwbs-event--pwbs_class-before-main")
        # PWBS Event Called in pwbs.__init__.main() after PWBS.main() is called (before quit)
        PWBS_EM.createEvent("pwbs-event--pwbs_class-after-main")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.__init__ after argparser being initialized
        PWBS_EM.createEvent("pwbs-event--pwbs_class-argparser-initilized")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.__init__ before parser_initializer being called
        PWBS_EM.createEvent("pwbs-event--pwbs_class-before-parser_initializer")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.__init__ after parser_initializer being called
        PWBS_EM.createEvent("pwbs-event--pwbs_class-after-parser_initializer")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.parser_initializer after specialtasks group is created
        PWBS_EM.createEvent("pwbs-event--pwbs_class-parser_initializer-specialtasks-groupcreated-start")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.parser_initializer after specialtasks group has added all PWBS special tasks
        PWBS_EM.createEvent("pwbs-event--pwbs_class-parser_initializer-specialtasks-groupcreated-end")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.parser_initializer after localconfigtasks group is created
        PWBS_EM.createEvent("pwbs-event--pwbs_class-parser_initializer-localconfigtasks-groupcreated")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.__init__ before PWBS Config Manager is created
        PWBS_EM.createEvent("pwbs-event--pwbs_class-before-configmanager-created")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.__init__ after PWBS Config Manager is created
        PWBS_EM.createEvent("pwbs-event--pwbs_class-after-configmanager-created")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.__init__ in "Try for errors" block if there are errors
        PWBS_EM.createEvent("pwbs-event--pwbs_class-configmanager-errored")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.localconfig_parser_initializer at start of function
        PWBS_EM.createEvent("pwbs-event--pwbs_class-localconfig_parser_initilizer-started")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.localconfig_parser_initializer on every element in CommandList object from Configuration Manager
        PWBS_EM.createEvent("pwbs-event--pwbs_class-localconfig_parser_initilizer-command-listitem")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.main before argparser.parse_args()
        PWBS_EM.createEvent("pwbs-event--pwbs_class-main-before-parseargs")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.main after argparser.parse_args()
        PWBS_EM.createEvent("pwbs-event--pwbs_class-main-after-parseargs")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.main before special_tasks_interpreter being called
        PWBS_EM.createEvent("pwbs-event--pwbs_class-main-before-specialtaskinterpreter")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.main after special_tasks_interpreter being called
        PWBS_EM.createEvent("pwbs-event--pwbs_class-main-after-specialtaskinterpreter")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.main before task_runner being called
        PWBS_EM.createEvent("pwbs-event--pwbs_class-main-before-taskinterpreter")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.main after task_runner being called
        PWBS_EM.createEvent("pwbs-event--pwbs_class-main-after-taskinterpreter")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.main on throwing NotImplmentedError
        PWBS_EM.createEvent("pwbs-event--pwbs_class-main-notimplementedfeatureerror")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before verbose Special Task
        PWBS_EM.createEvent("pwbs-event--before-specialtask-verbose")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before debug Special Task
        PWBS_EM.createEvent("pwbs-event--before-specialtask-debug")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before version Special Task
        PWBS_EM.createEvent("pwbs-event--before-specialtask-version")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before log Special Task
        PWBS_EM.createEvent("pwbs-event--before-specialtask-log")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before logfile Special Task
        PWBS_EM.createEvent("pwbs-event--before-specialtask-logfile")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before configfile Special Task
        PWBS_EM.createEvent("pwbs-event--before-specialtask-configfile")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before test_mode Special Task
        PWBS_EM.createEvent("pwbs-event--before-specialtask-test_mode")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before run_tests Special Task
        PWBS_EM.createEvent("pwbs-event--before-specialtask-run_tests")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before verbose Special Task
        PWBS_EM.createEvent("pwbs-event--after-specialtask-verbose")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after debug Special Task
        PWBS_EM.createEvent("pwbs-event--after-specialtask-debug")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after version Special Task
        PWBS_EM.createEvent("pwbs-event--after-specialtask-version")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after log Special Task
        PWBS_EM.createEvent("pwbs-event--after-specialtask-log")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after logfile Special Task
        PWBS_EM.createEvent("pwbs-event--after-specialtask-logfile")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after configfile Special Task
        PWBS_EM.createEvent("pwbs-event--after-specialtask-configfile")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after test_mode Special Task
        PWBS_EM.createEvent("pwbs-event--after-specialtask-test_mode")
        # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after run_tests Special Task
        PWBS_EM.createEvent("pwbs-event--after-specialtask-run_tests")
        # PWBS Event Called on start of PWBS
        PWBS_EM.createEvent("pwbs-event--start")
        # PWBS Event Called on exit of PWBS
        PWBS_EM.createEvent("pwbs-event--quit")
        # PWBS Event Called in test_runner on start of run_test function
        PWBS_EM.createEvent("pwbs-event--test-runner--start-run_test")
        # PWBS Event Called in test_runner on run test function
        PWBS_EM.createEvent("pwbs-event--test-runner--run-test-function")
        # PWBS Event Called in test_runner on end of run_test function
        PWBS_EM.createEvent("pwbs-event--test-runner--end-run_test")
        # PWBS Event Called in test_runner before test
        PWBS_EM.createEvent("pwbs-event--test-runner--before-test")
        # PWBS Event Called in test_runner after test
        PWBS_EM.createEvent("pwbs-event--test-runner--after-test")
        # PWBS Event Called on plugins initilization
        PWBS_EM.createEvent("pwbs-event--plugin-initilize")
        # Return PWBS Event Manager
        return PWBS_EM
