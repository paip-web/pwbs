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


class BaseLogger(object):
    """Base Logger Class
    Logging to STDOUT.
    """
    def __init__(self):
        """Constructor of the Class"""
        # Initiator of Debug Mode
        self.debug()
        # Initiator of Verbose Mode
        self.verbose()

    def debug(self, state=False):
        """Debug Mode Changer
        Args:
            state (bool): State to change to
                Defaults to False [Debug Mode Disabled].
        """
        # Inform when Debug Mode is turned on
        if state:
            print(prefix_text("Debug Mode turned on!"))
        # Change State Class Variable
        self.debug_state = state

    def verbose(self, state=1):
        """Verbose Mode Changer
        Args:
            state (int): State to change to
                Defaults to 1.
                Levels:
                    0: No Verbose
                    1: [Default] Small Verbose
                    2: Medium Verbose
                    3: Full Verbose
                    255: Extreme Verbose Mode
                        Debug Verbose Mode
        """
        # Change State Class Variable
        self.verbose_state = state
        # Log that verbose level changed
        self.log_verbose("Verbose Mode is now set to: {0}".format(state), 2)

    def log(self, text, prefix=prefix_text):
        """Log Function
        Args:
            text: Text to log
            prefix (function): Prefixer
                Defaults to Default PWBS Prefixer.
        """
        return print(prefix(text))

    def log_wop(self, text):
        """Log Function Without Prefixer
        Args:
            text: Text to log
        """
        return print(text)

    def log_verbose(self, text, verbose=1):
        """Log Verbose Function
        Args:
            text: Text to log
            verbose (int): Level to see that
                Defaults to 1.
        """
        # Checking is Verbose Level of message is good to log it
        if self.verbose_state >= verbose:
            return self.log(text)
        # Logging Debug info about message cannot be logged.
        return self.log_debug(
            "Verbose Logger doesn't succeed to log by set verbose level."
        )

    def log_debug(self, text):
        """Log Debug Function
        Args:
            text: Text to log
        """
        # Checking is Debug Mode Activated and logging
        if self.debug_state:
            return self.log("[DEBUG]: {0}".format(text))
        return None

    def log_assertion(self, assertion, name=None):
        """Log Assertion Function
        Args:
            assertion (bool): Assertion to test
            name (optional): Name of the assertion
        """
        # Try Assertion
        try:
            # Check Assertion
            assert assertion
            # If succeed then log good info
            if name is None:
                self.log_debug("Assertion succeed!")
            else:
                self.log_debug('Assertion "{0}" succeed!'.format(name))
        except AssertionError as e:
            # Assertion failed then log bad info
            if name is None:
                self.log_debug("Assertion failed!")
            else:
                self.log_debug('Assertion "{0}" failed!'.format(name))
            # ReRaise AsserionError
            raise LoggerAssertionError('Assertion failed!') from e


class LogLogger(BaseLogger):
    """Base Logger Class
    Logging to variable and can to file.
    """
    def __init__(self):
        """Constructor of the Class"""
        """Story Log Variable"""
        self.story = []
        """Running Base Logger Constructor"""
        super().__init__()

    def debug(self, state=False):
        """Debug Mode Changer
        Args:
            state (bool): State to change to
                Defaults to False [Debug Mode Disabled].
        """
        # Inform when Debug Mode is turned on
        if state:
            self.story.append(prefix_text("Debug Mode turned on!"))
        # Change State Class Variable
        self.debug_state = state

    def verbose(self, state=1):
        """Verbose Mode Changer
        Args:
            state (int): State to change to
                Defaults to 1.
                Levels:
                    0: No Verbose
                    1: [Default] Small Verbose
                    2: Medium Verbose
                    3: Full Verbose
                    255: Extreme Verbose Mode
                        Debug Verbose Mode
        """
        # Change State Class Variable
        self.verbose_state = state
        # Log that verbose level changed
        self.log_verbose("Verbose Mode is now set to: {0}".format(state), 2)

    def log(self, text, prefix=prefix_text):
        """Log Function
        Args:
            text: Text to log
            prefix (function): Prefixer
                Defaults to Default PWBS Prefixer.
        """
        return self.story.append(prefix(text))

    def log_wop(self, text):
        """Log Function Without Prefixer
        Args:
            text: Text to log
        """
        return self.story.append(text)

    def log_verbose(self, text, verbose=1):
        """Log Verbose Function
        Args:
            text: Text to log
            verbose (int): Level to see that
                Defaults to 1.
        """
        # Checking is Verbose Level of message is good to log it
        if self.verbose_state >= verbose:
            return self.log(text)
        # Logging Debug info about message cannot be logged.
        return self.log_debug(
            "Verbose Logger doesn't succeed to log by set verbose level."
        )

    def log_debug(self, text):
        """Log Debug Function
        Args:
            text: Text to log
        """
        # Checking is Debug Mode Activated and logging
        if self.debug_state:
            return self.log("[DEBUG]: {0}".format(text))
        return None

    def log_assertion(self, assertion, name=None):
        """Log Assertion Function
        Args:
            assertion (bool): Assertion to test
            name (optional): Name of the assertion
        """
        # Try Assertion
        try:
            # Check Assertion
            assert assertion
            # If succeed then log good info
            if name is None:
                self.log_debug("Assertion succeed!")
            else:
                self.log_debug('Assertion "{0}" succeed!'.format(name))
        except AssertionError as e:
            # Assertion failed then log bad info
            if name is None:
                self.log_debug("Assertion failed!")
            else:
                self.log_debug('Assertion "{0}" failed!'.format(name))
            # ReRaise AsserionError
            raise LoggerAssertionError('Assertion failed!') from e

    def log_file_write(self, file="pwbs.log"):
        """Log File Writer
        Args:
            file (:obj:`str`): Filename to write log
        """
        with open(file, mode="w") as f:
            f.writelines([x+"\n" for x in self.story])


class Logger(BaseLogger):
    """Logger Class
    Logging to variable and to STDOUT.
    """
    def __init__(self):
        """Constructor of the Class"""
        """Variable Logger"""
        self.log_logger = LogLogger()
        """Locker"""
        self.locker_log_logger = False
        """Running Base Logger Constructor"""
        super().__init__()

    def debug(self, state=False):
        """Debug Mode Changer
        Args:
            state (bool): State to change to
                Defaults to False [Debug Mode Disabled].
        """
        self.log_logger.debug(state)
        return super().debug(state)

    def verbose(self, state=1):
        """Verbose Mode Changer
        Args:
            state (int): State to change to
                Defaults to 1.
                Levels:
                    0: No Verbose
                    1: [Default] Small Verbose
                    2: Medium Verbose
                    3: Full Verbose
                    255: Extreme Verbose Mode
                        Debug Verbose Mode
        """
        self.log_logger.verbose(state)
        self.locker_log_logger = True
        ret = super().verbose(state)
        self.locker_log_logger = False
        return ret

    def log(self, text, prefix=prefix_text):
        """Log Function
        Args:
            text: Text to log
            prefix (function): Prefixer
                Defaults to Default PWBS Prefixer.
        """
        if not self.locker_log_logger:
            self.log_logger.log(text, prefix)
        return super().log(text, prefix)

    def log_wop(self, text):
        """Log Function Without Prefixer
        Args:
            text: Text to log
        """
        if not self.locker_log_logger:
            self.log_logger.log_wop(text)
        return super().log_wop(text)

    def log_verbose(self, text, verbose=1):
        """Log Verbose Function
        Args:
            text: Text to log
            verbose (int): Level to see that
                Defaults to 1.
        """
        if not self.locker_log_logger:
            self.log_logger.log_verbose(text, verbose)
        self.locker_log_logger = True
        ret = super().log_verbose(text, verbose)
        self.locker_log_logger = False
        return ret

    def log_debug(self, text):
        """Log Debug Function
        Args:
            text: Text to log
        """
        if not self.locker_log_logger:
            self.log_logger.log_debug(text)
        self.locker_log_logger = True
        ret = super().log_debug(text)
        self.locker_log_logger = False
        return ret

    def log_assertion(self, assertion, name=None):
        """Log Assertion Function
        Args:
            assertion (bool): Assertion to test
            name (optional): Name of the assertion
        """
        self.log_logger.log_assertion(assertion, name)
        self.locker_log_logger = True
        ret = super().log_assertion(assertion, name)
        self.locker_log_logger = False
        return ret

    def log_file_write(self, file="pwbs.log"):
        """Log File Writer
        Args:
            file (:obj:`str`): Filename to write log
        """
        return self.log_logger.log_file_write(file)

    def story(self):
        return self.log_logger.story
