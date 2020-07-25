# -*- coding: utf-8 -*-
"""PAiP Web Build System - Shell Runner Class

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from subprocess import run
from subprocess import Popen
from subprocess import PIPE
from typing import Dict
from pwbs.runner.runner import Runner

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


# Shell Runner Class


class ShellRunner(Runner):
    """Shell Runner Class"""

    def init(self):
        """
        Runner Initialization Method
        """
        pass

    @staticmethod
    def constants() -> Dict:
        """
        Shell Constants
        """
        return {
            "return_code": 0x1,
            "stdout": 0x2,
            "stderr": 0x3
        }

    @staticmethod
    def execute_and_capture(command: str):
        """
        Execute Command with capturing output
        :param command: Command
        """
        try:
            process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
            while True:
                output = process.stdout.readline()
                error_output = process.stderr.readline()
                if len(output) == 0 and len(error_output) == 0 and process.poll() is not None:
                    break
                if output:
                    yield ShellRunner.constants()['stdout'], output.strip()
                if error_output:
                    yield ShellRunner.constants()['stderr'], error_output.strip()
            rc = process.poll()
            yield ShellRunner.constants()['return_code'], rc
        except OSError:
            print("PWBS ERROR: Command {} could not execute!".format(command))
            yield None

    @staticmethod
    def execute_without_capture(command: str):
        """
        Execute Command without capturing output
        :param command: Command
        """
        try:
            if isinstance(command, list):
                for cmd in command:
                    yield run(cmd, shell=True, check=False)
            else:
                yield run(command, shell=True, check=False)
        except OSError:
            print("PWBS ERROR: Command {} could not execute!".format(command))
            yield None

    def execute(self, command: str, capture_output: bool = False, *args, **kwargs):
        """
        Command Execution Method
        """
        def execute_cmd(cmd: str):
            """
            Execute Command
            :param cmd: Command
            """
            if capture_output:
                return ShellRunner.execute_and_capture(cmd)
            return ShellRunner.execute_without_capture(cmd)

        if isinstance(command, list):
            for cmd in command:
                yield execute_cmd(cmd)
        else:
            yield execute_cmd(command)
