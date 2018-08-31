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
__version__ = '0.4.0-dev0'
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

def test(PWBS_EM: PWBSEventManager):
    funct = lambda event_name, *args, **kwargs: print("{0}: {1} | {2}".format(event_name, args, kwargs))
    # PWBS Event Called in pwbs.__init__.main() when PWBS class is initialized
    PWBS_EM.addHandler("pwbs-event--pwbs_class-initialized", funct)
    # PWBS Event Called in pwbs.__init__.main() before PWBS.main() is called
    PWBS_EM.addHandler("pwbs-event--pwbs_class-before-main", funct)
    # PWBS Event Called in pwbs.__init__.main() after PWBS.main() is called (before quit)
    PWBS_EM.addHandler("pwbs-event--pwbs_class-after-main", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.__init__ after argparser being initialized
    PWBS_EM.addHandler("pwbs-event--pwbs_class-argparser-initilized", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.__init__ before parser_initializer being called
    PWBS_EM.addHandler("pwbs-event--pwbs_class-before-parser_initializer", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.__init__ after parser_initializer being called
    PWBS_EM.addHandler("pwbs-event--pwbs_class-after-parser_initializer", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.parser_initializer after specialtasks group is created
    PWBS_EM.addHandler("pwbs-event--pwbs_class-parser_initializer-specialtasks-groupcreated-start", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.parser_initializer after specialtasks group has added all PWBS special tasks
    PWBS_EM.addHandler("pwbs-event--pwbs_class-parser_initializer-specialtasks-groupcreated-end", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.parser_initializer after localconfigtasks group is created
    PWBS_EM.addHandler("pwbs-event--pwbs_class-parser_initializer-localconfigtasks-groupcreated", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.__init__ before PWBS Config Manager is created
    PWBS_EM.addHandler("pwbs-event--pwbs_class-before-configmanager-created", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.__init__ after PWBS Config Manager is created
    PWBS_EM.addHandler("pwbs-event--pwbs_class-after-configmanager-created", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.__init__ in "Try for errors" block if there are errors
    PWBS_EM.addHandler("pwbs-event--pwbs_class-configmanager-errored", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.localconfig_parser_initializer at start of function
    PWBS_EM.addHandler("pwbs-event--pwbs_class-localconfig_parser_initilizer-started", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.localconfig_parser_initializer on every element in CommandList object from Configuration Manager
    PWBS_EM.addHandler("pwbs-event--pwbs_class-localconfig_parser_initilizer-command-listitem", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.main before argparser.parse_args()
    PWBS_EM.addHandler("pwbs-event--pwbs_class-main-before-parseargs", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.main after argparser.parse_args()
    PWBS_EM.addHandler("pwbs-event--pwbs_class-main-after-parseargs", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.main before special_tasks_interpreter being called
    PWBS_EM.addHandler("pwbs-event--pwbs_class-main-before-specialtaskinterpreter", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.main after special_tasks_interpreter being called
    PWBS_EM.addHandler("pwbs-event--pwbs_class-main-after-specialtaskinterpreter", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.main before task_runner being called
    PWBS_EM.addHandler("pwbs-event--pwbs_class-main-before-taskinterpreter", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.main after task_runner being called
    PWBS_EM.addHandler("pwbs-event--pwbs_class-main-after-taskinterpreter", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.main on throwing NotImplmentedError
    PWBS_EM.addHandler("pwbs-event--pwbs_class-main-notimplementedfeatureerror", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before verbose Special Task
    PWBS_EM.addHandler("pwbs-event--before-specialtask-verbose", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before debug Special Task
    PWBS_EM.addHandler("pwbs-event--before-specialtask-debug", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before version Special Task
    PWBS_EM.addHandler("pwbs-event--before-specialtask-version", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before log Special Task
    PWBS_EM.addHandler("pwbs-event--before-specialtask-log", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before logfile Special Task
    PWBS_EM.addHandler("pwbs-event--before-specialtask-logfile", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before configfile Special Task
    PWBS_EM.addHandler("pwbs-event--before-specialtask-configfile", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before test_mode Special Task
    PWBS_EM.addHandler("pwbs-event--before-specialtask-test_mode", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before run_tests Special Task
    PWBS_EM.addHandler("pwbs-event--before-specialtask-run_tests", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter before verbose Special Task
    PWBS_EM.addHandler("pwbs-event--after-specialtask-verbose", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after debug Special Task
    PWBS_EM.addHandler("pwbs-event--after-specialtask-debug", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after version Special Task
    PWBS_EM.addHandler("pwbs-event--after-specialtask-version", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after log Special Task
    PWBS_EM.addHandler("pwbs-event--after-specialtask-log", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after logfile Special Task
    PWBS_EM.addHandler("pwbs-event--after-specialtask-logfile", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after configfile Special Task
    PWBS_EM.addHandler("pwbs-event--after-specialtask-configfile", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after test_mode Special Task
    PWBS_EM.addHandler("pwbs-event--after-specialtask-test_mode", funct)
    # PWBS Event Called in pwbs.pwbs_class.PWBS.special_tasks_interpreter after run_tests Special Task
    PWBS_EM.addHandler("pwbs-event--after-specialtask-run_tests", funct)
    # PWBS Event Called on start of PWBS
    PWBS_EM.addHandler("pwbs-event--start", funct)
    # PWBS Event Called on exit of PWBS
    PWBS_EM.addHandler("pwbs-event--quit", funct)
    # PWBS Event Called in test_runner on start of run_test function
    PWBS_EM.addHandler("pwbs-event--test-runner--start-run_test", funct)
    # PWBS Event Called in test_runner on run test function
    PWBS_EM.addHandler("pwbs-event--test-runner--run-test-function", funct)
    # PWBS Event Called in test_runner on end of run_test function
    PWBS_EM.addHandler("pwbs-event--test-runner--end-run_test", funct)
    # PWBS Event Called in test_runner before test
    PWBS_EM.addHandler("pwbs-event--test-runner--before-test", funct)
    # PWBS Event Called in test_runner after test
    PWBS_EM.addHandler("pwbs-event--test-runner--after-test", funct)

def main():
    # Initialize PWBS Event Manager
    PWBS_EM = PWBSEventManager.initialize()
    test(PWBS_EM)
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
