pwbs.tests
---------------

.. py:module:: pwbs.tests

This module is place for PWBS tests.

Test Runner
"""""""""""
.. py:exception:: TestSucceed()

    Exception for Passed Test

.. py:exception:: TestFailed()

    Exception for Failed Test

.. py:function:: tests_prefix_text(text)

    Test Runner Prefixer

    :argument str text: Text to Prefixer

.. py:function:: run_test(test_function, test_name: str, test_comment: str, test_module: str, test_except_to_fail=False)

    Function for running tests in Test Runner.
    
    :argument function test_function: Test Function
    :argument str test_name: Name of the Test
    :argument str test_comment: Comment of the Test
    :argument str test_module: Tested Module
    :argument bool test_except_to_fail: Test Excepted to Fail

.. py:function:: test_runner()

    Test Runner


Tests
"""""

.. py:module:: pwbs.tests.test_0

Test 0
******

.. py:function:: test_0_0()

    Test testing assertions

.. py:function:: test_0_1()

    Test testing excepted failed assertions

.. py:module:: pwbs.tests.test_1

Test 1
******

.. py:function:: test_1_0()

    Checking :py:class:`pwbs.command.command.CommandType`

.. py:function:: test_1_1()

    Checking :py:class:`pwbs.command.command.Platform`

.. py:function:: test_1_2()

    Checking :py:class:`pwbs.command.command.CommandMode`

.. py:function:: test_1_3()

    Checking :py:class:`pwbs.command.command.Command`
    
    Tested:
    
    * Command.__init__()
    
    * Command.__eq__()

.. py:function:: test_1_4()

    Checking :py:class:`pwbs.command.command.Command`

    Tested:

    * Command.run()

    * Command.argument_parser()

.. py:function:: test_1_5()

    Checking :py:class:`pwbs.command.command.Command`

    Tested:

    * Command.execute_as_singletask_or_multicommand()

.. py:function:: test_1_6()

    Checking :py:class:`pwbs.command.command.Command`

    Tested:

    * Command.execute_as_watcher() [TODO: Testing NotImplementedFeatureError]

.. py:function:: test_1_7()

    Checking :py:class:`pwbs.command.command.Command`

    Tested:

    * Command.execute_as_scheduler()

.. py:function:: test_1_8()

    Checking :py:class:`pwbs.command.command.Command`

    Tested:

    * Command.__add__()

.. py:function:: test_1_9()

    Checking :py:class:`pwbs.command.command.CommandList`

.. py:module:: pwbs.tests.test_2

Test 2
******

.. py:function:: test_2_0()

    Checking :py:mod:`pwbs.config.config_manager` Exceptions Tests

.. py:function:: test_2_1()

    Checking :py:class:`pwbs.config.config_manager.ConfigManager`

.. py:function:: test_2_2()

    Checking :py:class:`pwbs.config.pwbs_config.PWBS_ConfigManager`

.. py:module:: pwbs.tests.test_3

Test 3
******

.. py:function:: test_3_0()

    Checking :py:exc:`pwbs.core.NotImplementedFeatureError`

.. py:function:: test_3_1()

    Checking :py:exc:`pwbs.core.prefix_text`


Test 4
******

Test has been deleted in commit: ``db38a705d725e65c999843e3f25f84a4b201ec54``.
This test has been deleted by copying Test 5.

.. py:module:: pwbs.tests.test_5


Test 5
******

.. py:function:: test_5_0()

    Checking :py:exc:`pwbs.log.logger.LoggerAssertionError`

.. py:function:: test_5_1()

    Checking :py:class:`pwbs.log.logger.BaseLogger`

.. py:function:: test_5_2()

    Checking :py:class:`pwbs.log.logger.LogLogger`

.. py:function:: test_5_3()

    Checking :py:class:`pwbs.log.logger.Logger`
