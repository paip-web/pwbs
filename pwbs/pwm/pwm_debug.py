#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Module - Debug

This module creates Debug decorator as well as ProgramConfiguration class which can be used to Configure Program and Debug Mode

NAME - PAiP Web Module - Debug
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
VERSION - v.0.0.0.2

Examples:
    Example 1:
        # Using a ProgramConfiguration Class to handle decorator
        from lib.pwm.pwm_debug import ProgramConfiguration
        ProgramConf = ProgramConfiguration()
        ProgramConf.SetDebugMode(True)
        @ProgramConf.debug
        def main(name):
            return print("Hello", name)
        main("Patryk")
    Example 2:
        # Using decorator directly
        from lib.pwm.pwm_debug import debug
        @debug(True)
        def main(name):
            return print("Hello", name)
        main("Patryk")

Todo:
    * Probably Change ProgramConfiguration Class and make in pwm_programconfig.py

"""
### Imports
# Timing
from time import time
# Getting Source and file of function
from inspect import getsource, getfile
# Getting ProgramBaseConfiguration Class
from pwm_programbaseconfig import ProgramBaseConfiguration
### Functions

def print_debug(name, *args, **kwargs):
    """Printing Debug

    Function to display formatted output in decorator options
    Args:
        name: Name of Process [like "Function Source:"]
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    Returns:
        called print function
    """
    return print("DEBUG|", name, *args, **kwargs)

def debug(
        verbose_mode=False,
        function_name=False,
        argument_listing=False,
        source_listing=False,
        file_listing=False,
        return_listing=False,
        error_listing=False,
        timing_listing=False
    ):
    """Debug Decorator

    It's decorator to debug wrapped function.
    If you want to don't want debug decorator without deleting code use Program Configuration way or use @debug() as decorator [Without paramaters].
    If you want full debug mode use @debug(True).
    If you want specific debug mode than use keyword arguments.

    Args:
        verbose_mode (bool, optional): Verbose Mode. Turns on full debug mode. Defaults to False.
        function_name (bool, optional): Printing to Command Line wrapped function name. Defaults to False.
        argument_listing (bool, optional): Printing to Command Line wrapped function parameters. Defaults to False.
        source_listing (bool, optional): Printing to Command Line wrapped function source code. Defaults to False.
        file_listing (bool, optional): Printing to Command Line in what file wrapped function is. Defaults to False.
        return_listing (bool, optional): Printing to Command Line wrapped function return. Defaults to False.
        error_listing (bool, optional): Printing to Command Line wrapped function error. If False then try code and catch exception raising another. Defaults to False.
        timing_listing (bool, optional): Printing to Command Line wrapped function timing. Defaults to False.

    """
    def f1(f):
        def f2(*args, **kwargs):
            if function_name or verbose_mode:
                print_debug("Function Name:", f.__name__)
            if argument_listing or verbose_mode:
                print_debug("Function Args:", str(args), str(kwargs))
            if source_listing or verbose_mode:
                print_debug("Function Source:\n", getsource(f))
            if file_listing or verbose_mode:
                print_debug("Function is in:", getfile(f))
            try:
                before = time()
                ret = f(*args, **kwargs)
                after = time()
                elapsed = after - before
                if timing_listing or verbose_mode:
                    print_debug("Elapsed time:", elapsed)
            except Exception as ex:
                if error_listing or verbose_mode:
                    print_debug("Catched:", str(ex))
                else:
                    raise ex
            if return_listing or verbose_mode:
                print_debug("Function Returned:", ret)
            return ret
        return f2
    return f1

class ProgramConfiguration(ProgramBaseConfiguration):
    """Program Conguration Class

    Attributes:
        args (object): Arguments provided through constructor
        kwargs (object): Keyword Arguments provided through constructor
        debug (function): Function which can be used as decorator but it doesn't need arguments by configuration which is in class
        debug_verbose (object): Full Debug Mode Variable
        debug_mode_a (object): Debug Mode Arguments
        debug_mode_k (object): Debug Mode Keyword Arguments

    """
    def __init__(self, *args, **kwargs):
        """Init Method

        Constructor of class
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.args, self.kwargs = args, kwargs
        self.SetDebugMode(False)
        self.debug = debug(self.debug_verbose, self.debug_mode_a, self.debug_mode_k)
    def SetDebugMode(self, verbose_mode, *args, **kwargs):
        """Method Setting Debug Mode

        Function to change Debug Mode it also changes debug variable in class(which can be used as decorator) to use new debug mode
        Args:
            verbose_mode (bool): Full Debug Mode Variable. Here it doesn't have default because in constructor debug is default made to have Off Debug Mode
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.debug_verbose = verbose_mode
        self.debug_mode_a, self.debug_mode_k = args, kwargs
        self.debug = debug(self.debug_verbose, self.debug_mode_a, self.debug_mode_k)
