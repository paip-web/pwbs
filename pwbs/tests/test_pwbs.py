# Imports
import pytest
# Test Subject Imports
from pwbs.__pwbs import *
from pwbs.command_interpreter import *
from pwbs.commands_special import *
from pwbs.pwbs import *
# Classes and Functions

# Tests for v__pwbs.py
def fntest(a):
    return a
@pytest.mark.parametrize("ver, level, expect", [
    (0, ">0", 0xFF),
    (0, ">1", 0xFF),
    (0, ">2", 0xFF),
    (0, ">3", 0xFF),
    (0, ">255", 0xFF),
    (0, "==0", 0),
    (1, "==1", 0),
    (2, "==2", 0),
    (3, "==3", 0),
    (255, "==255", 0),
    (0, "<0", 0xFF),
    (0, "<1", 0),
    (0, "<2", 0),
    (0, "<3", 0),
    (0, "<255", 0)
])
def test__underscorepwbs_f1_t1(ver, level, expect):
    assert verboseSpecific(ver, level, fntest, [0]) == expect

@pytest.mark.parametrize("string, regex", [
    ("test", "^te$"),
    ("test", "[0-9]+"),
    ("test", "[A-Z]+"),
    ("test", "[a-z]{5}")
])
def test__underscorepwbs_f2_t1(string, regex):
    assert regexString(string, regex) is None

@pytest.mark.parametrize("string, regex", [
    ("test","test"),
    ("test", "[a-z]"),
    ("test", "[a-z]{4}"),
    ("test", "\S+"),
    ("test", "[A-z0-9]+")
])
def test__underscorepwbs_f2_t2(string, regex):
    assert regexString(string, regex) is not None

# NO TESTS YET FOR:
"""
* command_interpreter.py | Dynamic Changes
* commands_special.py | Dynamic Changes
* pwbs.py | Dynamic Changes
"""
