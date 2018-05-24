pwbs.log.logger
---------------

.. py:module:: pwbs.log.logger

This module is place for PWBS logging things.

.. py:exception:: LoggerAssertionError()

    Error to show when Logger.log_assertion failed assertion.

.. py:class:: BaseLogger()

    Base Logger Class

    That Logger logging to STDOUT.

    .. py:attribute:: debug_delayed_story
    
        Story Log for Delayed Debug

    .. py:attribute:: debug_state
    
        Debug Mode State

    .. py:attribute:: verbose_state
    
        Verbose Mode State

    .. py:method:: debug(state=False)
    
        Debug Mode Changer

        :argument bool state: State to change to

            Defaults to False. [Debug Mode Disabled]

    .. py:method:: verbose(state=1)
    
        Verbose Mode Changer

        :argument int state: State to change to
        
            Defaults to 1.

            Levels:

            0. No Verbose

            1. Small Verbose

            2. Medium Verbose

            3. Full Verbose

            255. Debug Verbose Mode

    .. py:method:: log(text, prefix=pwbs.core.prefix_text)
    
        Log Function

        :argument str text: Text to Log
        :argument function prefix: Prefixer to Use

    .. py:method:: log_wop(text)
    
        Log Function [Without prefixer]

        :argument str text: Text to Log

    .. py:method:: log_verbose(text, verbose=1)
    
        Log Verbose Function (Logs when message verbose is smaller than Configuration Verbosity)

        :argument str text: Text to Log
        :argument int verbose: Verbose Level for Message

            Defaults to 1.

    .. py:method:: log_debug(text)
    
        Log Debug Function (Logs when debug mode is turned on)

        :argument str text: Text to Log

    .. py:method:: log_assertion(assertion, name=None)
    
        Log Assertion Function

        :argument bool assertion: Assertion to check
        :argument str name: Name of the Assertion [To name Log Assertions]
    

.. py:class:: LogLogger()

    Log Logger Class

    That Logger logging to file.

    .. py:attribute:: story = []
    
        Story Log

    .. py:attribute:: logfile = "pwbs.log"
    
        Log File Variable

    .. py:attribute:: activelogging = False
    
        Active Logging Variable

        When Active Logging is active then every any log function call it save to log file.

    .. py:attribute:: debug_delayed_story
    
        Story Log for Delayed Debug

    .. py:attribute:: debug_state
    
        Debug Mode State

    .. py:attribute:: verbose_state
    
        Verbose Mode State

    .. py:method:: debug(state=False)
    
        Debug Mode Changer

        :argument bool state: State to change to

            Defaults to False. [Debug Mode Disabled]

    .. py:method:: verbose(state=1)
    
        Verbose Mode Changer

        :argument int state: State to change to
        
            Defaults to 1.

            Levels:

            0. No Verbose

            1. Small Verbose

            2. Medium Verbose

            3. Full Verbose

            255. Debug Verbose Mode

    .. py:method:: log(text, prefix=pwbs.core.prefix_text)
    
        Log Function

        :argument str text: Text to Log
        :argument function prefix: Prefixer to Use

    .. py:method:: log_wop(text)
    
        Log Function [Without prefixer]

        :argument str text: Text to Log

    .. py:method:: log_verbose(text, verbose=1)
    
        Log Verbose Function (Logs when message verbose is smaller than Configuration Verbosity)

        :argument str text: Text to Log
        :argument int verbose: Verbose Level for Message

            Defaults to 1.

    .. py:method:: log_debug(text)
    
        Log Debug Function (Logs when debug mode is turned on)

        :argument str text: Text to Log

    .. py:method:: log_assertion(assertion, name=None)
    
        Log Assertion Function

        :argument bool assertion: Assertion to check
        :argument str name: Name of the Assertion [To name Log Assertions]
    
    .. py:method:: log_file_write(file=None)
    
        Log File Writer

        :argument str file: Filename to write log.
            
            Defaults to None. (Which using self.logfile class attribute)

.. py:class:: Logger()

    Logger Class

    That Logger logging to file and STDOUT.

    .. py:attribute:: log_logger = pwbs.log.logger.LogLogger()
    
        File Logger

    .. py:attribute:: locker_log_logger = False
    
        Log Logger Lock Variable

    .. py:attribute:: debug_delayed_story
    
        Story Log for Delayed Debug

    .. py:attribute:: debug_state
    
        Debug Mode State

    .. py:attribute:: verbose_state
    
        Verbose Mode State

    .. py:method:: debug(state=False)
    
        Debug Mode Changer

        :argument bool state: State to change to

            Defaults to False. [Debug Mode Disabled]

    .. py:method:: verbose(state=1)
    
        Verbose Mode Changer

        :argument int state: State to change to
        
            Defaults to 1.

            Levels:

            0. No Verbose

            1. Small Verbose

            2. Medium Verbose

            3. Full Verbose

            255. Debug Verbose Mode

    .. py:method:: log(text, prefix=pwbs.core.prefix_text)
    
        Log Function

        :argument str text: Text to Log
        :argument function prefix: Prefixer to Use

    .. py:method:: log_wop(text)
    
        Log Function [Without prefixer]

        :argument str text: Text to Log

    .. py:method:: log_verbose(text, verbose=1)
    
        Log Verbose Function (Logs when message verbose is smaller than Configuration Verbosity)

        :argument str text: Text to Log
        :argument int verbose: Verbose Level for Message

            Defaults to 1.

    .. py:method:: log_debug(text)
    
        Log Debug Function (Logs when debug mode is turned on)

        :argument str text: Text to Log

    .. py:method:: log_assertion(assertion, name=None)
    
        Log Assertion Function

        :argument bool assertion: Assertion to check
        :argument str name: Name of the Assertion [To name Log Assertions]
    
    .. py:method:: log_file_write(file=None)
    
        Log File Writer

        :argument str file: Filename to write log.
            
            Defaults to None. (Which using self.logfile class attribute)

    .. py:method:: story()
    
        Log Logger Story Variable Getter

        :returns: :py:attr:`pwbs.log.logger.Logger.log_logger.story`
        :rtype: :py:class:`list`