# Imports
import pytest
from os import path
# Test Subject Imports
from pwbs.pwm.pwm_debug import *
from pwbs.pwm.pwm_exec import *
from pwbs.pwm.pwm_json import *
from pwbs.pwm.pwm_system import *
from pwbs.pwm.pwm_watcher import *
from pwbs.__pwbs import regexString
# Classes and Functions

# Test for execute() from pwm_exec.py | Single Command
def test_execpwm_f1_t1():
    result = execute("echo Hello")
    assert result is not None
    #assert result == b'Hello\r\n'
    assert regexString(result.decode("utf-8"), r"Hello(\r|\n|\r\n)") is not None


# Test for execute() from pwm_exec.py | Multi Command
def test_execpwm_f1_t2():
    result = execute(["echo Hello", "echo Hello", "echo Hello", "echo Hello", "echo Hello"])
    assert result is not None
    #assert result == "b'Hello\\r\\n'b'Hello\\r\\n'b'Hello\\r\\n'b'Hello\\r\\n'b'Hello\\r\\n'"
    assert regexString(result, r"(b\'Hello(\\r|\\n|\\r\\n)\')+") is not None

# Test for read_json and write_json from pwm_json.py
def test_jsonpwm_f1x2_t1():
    script_cwd = path.abspath(path.dirname(__file__))
    if SystemVersion().system_system == "Windows":
        path_to_file = script_cwd+"\\test.json"
    else:
        path_to_file = script_cwd+"/test.json"
    data = read_json(path_to_file)
    print(data)
    assert data["test"] == "pass"
    assert write_json(path_to_file, data)

# Test for JSON_IO Class from pwm_json.py
def test_jsonpwm_c1_t1():
    script_cwd = path.abspath(path.dirname(__file__))
    if SystemVersion().system_system == "Windows":
        path_to_file = script_cwd+"\\test.json"
    else:
        path_to_file = script_cwd+"/test.json"
    datamanager = JSON_IO(path_to_file)
    data = datamanager.read()
    print(data)
    assert data["test"] == "pass"
    assert data == datamanager.write(data)

# NO TESTS YET FOR:
"""
* pwm_debug.py | No good ideas how to test debug decorator
* pwm_system.py | No good ideas how to test Informations about System function
* pwm_watcher.py | No good ideas and too big mess in that file
"""
