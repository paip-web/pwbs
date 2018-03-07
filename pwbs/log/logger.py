# -*- coding: utf-8 -*-
"""PAiP Web Build System - Logger

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from __future__ import print_function
from ..core import prefix_text

# Class Definition


class LoggerAssertionError(AssertionError):
    """Error to show when Logger.log_assertion failed assertion."""
    pass


# TO_TEST:
class BaseLogger(object):
    """Base Logger Class"""
    def __init__(self):
        self.debug()
        self.verbose()

    def debug(self, state=False):
        if state:
            print(prefix_text("Debug Mode turned on!"))
        self.debug_state = state

    def verbose(self, state=1):
        self.verbose_state = state
        self.log_verbose("Verbose Mode is now set to: {0}".format(state), 2)

    def log(self, text, prefix=prefix_text):
        return print(prefix(text))

    def log_wop(self, text):
        return print(text)

    def log_verbose(self, text, verbose=1):
        if self.verbose_state >= verbose:
            return self.log(text)
        return self.log_debug(
            "Verbose Logger doesn't succeed to log by set verbose level."
        )

    def log_debug(self, text):
        if self.debug_state:
            return self.log("[DEBUG]: {0}".format(text))
        return None

    def log_assertion(self, assertion, name=None):
        try:
            assert assertion
            if name is None:
                self.log_debug("Assertion succeed!")
            else:
                self.log_debug('Assertion "{0}" succeed!'.format(name))
        except AssertionError as e:
            if name is None:
                self.log_debug("Assertion failed!")
            else:
                self.log_debug('Assertion "{0}" failed!'.format(name))
            raise LoggerAssertionError('Assertion failed!') from e


# TO_TEST:
class LogLogger(BaseLogger):
    def __init__(self):
        self.story = []
        super().__init__()

    def debug(self, state=False):
        if state:
            self.story.append(prefix_text("Debug Mode turned on!"))
        self.debug_state = state

    def verbose(self, state=1):
        self.story.append(
            prefix_text("Verbose Mode is now set to: {0}".format(state))
        )
        self.verbose_state = state

    def log(self, text, prefix=prefix_text):
        return self.story.append(prefix(text))

    def log_wop(self, text):
        return self.story.append(text)

    def log_verbose(self, text, verbose=1):
        if self.verbose_state >= verbose:
            return self.log(text)
        return self.log_debug(
            "Verbose Logger doesn't succeed to log by set verbose level."
        )

    def log_debug(self, text):
        if self.debug_state:
            return self.log("[DEBUG]: {0}".format(text))
        return None

    def log_assertion(self, assertion, name=None):
        try:
            assert assertion
            if name is None:
                self.log_debug("Assertion succeed!")
            else:
                self.log_debug('Assertion "{0}" succeed!'.format(name))
        except AssertionError as e:
            if name is None:
                self.log_debug("Assertion failed!")
                self.story.append(prefix_text("Assertion failed!"))
            else:
                self.log_debug('Assertion "{0}" failed!'.format(name))
                self.story.append(
                    prefix_text('Assertion "{0}" failed!'.format(name))
                )
            raise LoggerAssertionError('Assertion failed!') from e

    def log_file_write(self, file="pwbs.log"):
        with open(file, mode="w") as f:
            f.writelines([x+"\n" for x in self.story])


# TO_TEST:
class Logger(BaseLogger):
    def __init__(self):
        self.log_logger = LogLogger()
        super().__init__()

    def debug(self, state=False):
        self.log_logger.debug(state)
        return super().debug(state)

    def verbose(self, state=1):
        self.log_logger.verbose(state)
        return super().verbose(state)

    def log(self, text, prefix=prefix_text):
        self.log_logger.log(text, prefix)
        return super().log(text, prefix)

    def log_wop(self, text):
        self.log_logger.log_wop(text)
        return super().log_wop(text)

    def log_verbose(self, text, verbose=1):
        self.log_logger.log_verbose(text, verbose)
        return super().log_verbose(text, verbose)

    def log_debug(self, text):
        self.log_logger.log_debug(text)
        return super().log_debug(text)

    def log_assertion(self, assertion, name=None):
        self.log_logger.log_assertion(assertion, name)
        return super().log_assertion(assertion, name)
