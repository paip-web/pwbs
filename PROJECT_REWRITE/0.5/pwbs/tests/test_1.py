# -*- coding: utf-8 -*-
"""PAiP Web Build System - Test

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT

"""
# Documentation
"""
Test 1
================
Tests for v0.4.0dev0 | pwbs.command
================
Test 1.0 - CommandType(Enum)
Test 1.1 - Platform(Enum)
Test 1.2 - CommandMode(Enum)
Test 1.3 - 1.8 - Command(object)
Test 1.9 - CommandList(object)
"""
# Test Function


def test_1_0():
    """Testing CommandType"""
    # Import
    from ..command.command import CommandType
    # Values
    assert CommandType.NullTask == CommandType(0x000)
    assert CommandType.InitialNullTask == CommandType(0x001)
    assert CommandType.SpecialTask == CommandType(0x101)
    assert CommandType.SingleTask == CommandType(0x201)
    assert CommandType.MultiTask == CommandType(0x202)
    assert CommandType.MultiCommandTask == CommandType(0x203)
    assert CommandType.WatcherTask == CommandType(0x204)
    assert CommandType.SchedulerTask == CommandType(0x205)
    assert CommandType.TestTask == CommandType(0xFF0)
    assert CommandType.ErrorTask == CommandType(0xFF1)
    assert CommandType.NullTaskF == CommandType(0xFFF)


def test_1_1():
    """Testing Platform"""
    # Import
    from ..command.command import Platform
    # Values
    assert Platform.NullOS == Platform(0b0000)
    assert Platform.Windows == Platform(0b0001)
    assert Platform.Linux == Platform(0b0010)
    assert Platform.MacOS == Platform(0b0100)
    assert Platform.Other == Platform(0b1000)
    assert Platform.Any == Platform(0b1111)


def test_1_2():
    """Testing CommandMode"""
    # Import
    from ..command.command import CommandMode
    # Values
    assert CommandMode.SingleTask_Standard == CommandMode(0x22010001)
    assert CommandMode.MultiTask_Standard == CommandMode(0x22020001)
    assert CommandMode.MultiCommandTask_Standard == CommandMode(0x22030001)
    assert CommandMode.WatcherTask_StartAndRun == CommandMode(0x22040001)
    assert CommandMode.WatcherTask_StartAndWait == CommandMode(0x22040002)
    assert CommandMode.SchedulerTask_StartAndRun == CommandMode(0x22050001)
    assert CommandMode.SchedulerTask_StartAndWait == CommandMode(0x22050002)
    assert CommandMode.NullMode == CommandMode(0x00000000)
    assert CommandMode.ModeNotSpecified == CommandMode(0x00000001)
    assert CommandMode.TestTask_TestMode == CommandMode(0xFFF00000)
    assert CommandMode.ErrorTask_ErrorMode == CommandMode(0xFFF1FFFF)
    assert CommandMode.NullTask_NullMode == CommandMode(0xF000FFF0)
    assert CommandMode.NullTaskF_NullMode == CommandMode(0xFFFFFFF0)
    assert CommandMode.ErrorMode == CommandMode(0xFFFFFFFF)


def test_1_3():
    """Testing Command"""
    # Import
    from ..command.command import Command
    # Tests
    # Command.__init__()
    test_variable = Command("test_1_3")
    assert test_variable is not None
    test_variable._log.log("Test 1.3")
    # Command.__init__() Variables and Defaults
    from ..log.logger import Logger
    assert isinstance(test_variable._log, Logger)
    assert test_variable.name == "test_1_3"
    from ..command.command import CommandType, CommandMode, Platform
    assert test_variable.type == CommandType.InitialNullTask
    assert test_variable.commands is None
    assert test_variable.comment == ""
    assert test_variable.mode == CommandMode.NullMode
    assert test_variable.arguments is None
    assert test_variable.special is None
    assert test_variable.platform == Platform.Any
    # Command.__eq__()
    test_variable__2 = Command("test_1_3")
    assert test_variable == test_variable__2
    assert test_variable == "test_1_3"
    assert test_variable__2 == "test_1_3"


def test_1_4():
    """Testing Command"""
    # Import
    from ..command.command import Command, CommandType, CommandMode
    # Command.run()
    # TO_TEST: More Tests on that
    test_variable__3 = Command(
        "test_1_3",
        CommandType.TestTask,
        None,
        "",
        CommandMode.TestTask_TestMode)
    assert test_variable__3.run() == "TESTED"
    # Command.argument_parser()
    assert test_variable__3.comment == test_variable__3.argument_parser()


def test_1_5():
    """Testing Command"""
    # Import
    from ..command.command import Command, CommandType, CommandMode
    # Command.execute_as_singletask_or_multicommand()
    test_variable__6 = Command("test_1_3", CommandType.SingleTask, ["echo If you see this that means test 1.3 Works!"], "Test 1.3", CommandMode.SingleTask_Standard)
    test_variable__6.run()


def test_1_6():
    """Testing Command"""
    # Import
    from ..command.command import Command, CommandType, CommandMode
    # Command.execute_as_watcher()
    test_variable__7 = Command(
        "test_1_3",
        CommandType.TestTask,
        None,
        "",
        CommandMode.TestTask_TestMode)
    from ..core import NotImplementedFeatureError
    try:
        test_variable__7.execute_as_watcher()
    except NotImplementedFeatureError:
        pass


def test_1_7():
    """Testing Command"""
    # Import
    from ..command.command import Command, CommandMode, CommandType
    # Command.execute_as_scheduler()
    test_variable__8 = Command(
        "test_1_3",
        CommandType.TestTask,
        None,
        "",
        CommandMode.TestTask_TestMode)
    from ..core import NotImplementedFeatureError
    try:
        test_variable__8.execute_as_watcher()
    except NotImplementedFeatureError:
        pass


def test_1_8():
    """Testing Command"""
    # Import
    from ..command.command import Command, CommandType
    # Command.__add__()
    test_table = ["t1", "t2"]
    test_variable__4 = Command("test_1_3", CommandType.TestTask, [test_table[0]])
    test_variable__5 = Command("test_1_3", CommandType.TestTask, [test_table[1]])
    test_var = (test_variable__4.commands + test_variable__5.commands)
    test_res = (test_variable__4 + test_variable__5)
    assert test_res.commands == test_var
    assert test_res.commands == test_table


def test_1_9():
    """Testing CommandList"""
    # Import
    from ..command.command import Command, CommandList
    # Test Vars
    test_var_1 = Command("test_1_9_1")
    test_var_2 = Command("test_1_9_2")
    test_var_3 = Command("test_1_9_3")
    test_var_4 = Command("test_1_9_4")
    test_var_5 = Command("test_1_9_5")
    # CommandList.__init__()
    test_table = [test_var_1, test_var_2, test_var_3]
    test_var = CommandList(test_table)
    assert test_var.values == test_table
    # CommandList.__getitem__()
    for i in range(0, len(test_table)):
        assert test_var[test_table[i].name].name == test_table[i].name
    # CommandList.__setitem__()
    test_var[test_var_3.name] = test_var_5
    assert test_var[test_var_5.name].name == test_var_5.name
    # # New Item
    test_var[test_var_4.name] = test_var_4
    print(test_var[test_var_4.name].name)
    # CommandList.__delitem__()
    del test_var[test_var_4.name]
    try:
        test = test_var[test_var_4.name]
        assert False
        assert test is not None
    except KeyError:
        pass
    # CommandList.__contains__()
    assert test_var_1.name in test_var
    # CommandList.items()
    assert test_var.items() is test_var.values
