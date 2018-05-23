pwbs.pwbs_class
---------------

.. py:module:: pwbs.pwbs_class

This module is place for main PWBS Program Class.

.. py:class:: PWBS
    This class is main PWBS Program Class.

Constructor is making these steps:

* Making Argument Parser [Parser of CLI Arguments]

* Initialize Parser

* Making PWBS Config Manager Object

* Check for errors of PWBS Config Manager Object

* Initialize Config Manager

.. py:method:: PWBS.parser_initializer(self)
    This method is to initalize parser.

This method is making these steps:

* Making Special Tasks Argument Group

* Adding Special Tasks Commands: [--verbose, --debug, --version, --new-config, --log, --log-file, --config-file, --test-mode, --run-tests]

* Adding Task Argument [This argument takes everything which is after special tasks commands or everything if there isn't any special task command]

* Adding Local Configuration Tasks Argument Group

.. py:method:: PWBS.localconfig_parser_initializer(self)
    This method is to initalize parser of local configuration.
    
This method is: 

* Trying to change json tasks into Commands Class Object changing it into one CommandList Class Object with all commands.

.. py:method:: PWBS.special_tasks_interpreter(self)
    This method is to interpret special tasks.

This method is:

* Checking is any of special task was called.

* If yes then it executes that special task that was called.

.. py:method:: PWBS.task_runner(self)
    This method is to run local configurations tasks.

This method is:

* Calling run method on every Command object that was called.

.. py:method:: PWBS.main(self)
    This method is main function of Program.

This method is:

* Parsing Arguments
* Interpreting Special Tasks
* Interpreting Normal Tasks