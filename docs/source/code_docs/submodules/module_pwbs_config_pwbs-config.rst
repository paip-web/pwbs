pwbs.config.pwbs_config
-----------------------

.. py:module:: pwbs.config.pwbs_config

This module is place for PWBS Configuration Manager.

.. py:class:: PWBS_ConfigManager()

    This class is holding PWBS Config Manager.

    .. py:attribute:: log = pwbs.log.logger.Logger()
    
        Logger

    .. py:attribute:: verbose = 1
    
        Verbose Level

    .. py:attribute:: debug = False
    
        Debug Mode

    .. py:attribute:: configmanager = pwbs.config.configmanager.ConfigManager()
    
        Local Configuration File Manager

    .. py:attribute:: commands = pwbs.command.command.CommandList([])
    
        Commands List

    .. py:method:: config_file()
    
        Configuration File Loader

        :returns: Data from Configuration File
        :rtype: dict
    
    .. py:method:: commands_to_commandlist()
    
        Method for changing Configuration File Data to CommandList Object

        :raises PWBSInvalidConfigFile: Invalid Configuration File

    .. py:staticmethod:: ctcl__cmdtype(commandbody)
    
        This method is to change Command Dict Object into :py:class:`pwbs.command.command.CommandType`.

        :argument dict commandbody: Command Dict Object

    .. py:staticmethod:: ctcl__comment(commandbody)
    
        This method is to change Command Dict Object into :py:class:`str` with comment.

        :argument dict commandbody: Command Dict Object

    .. py:staticmethod:: ctcl__cmdmode(commandbody)
    
        This method is to change Command Dict Object into :py:class:`pwbs.command.command.CommandMode`.

        :argument dict commandbody: Command Dict Object

    .. py:staticmethod:: ctcl__arguments(commandbody)
    
        This method is to change Command Dict Object into :py:class:`list` with arguments.

        :argument dict commandbody: Command Dict Object

    .. py:staticmethod:: ctcl__commands(commandbody)
    
        This method is to change Command Dict Object into :py:class:`list` with commands.

        :argument dict commandbody: Command Dict Object

    .. py:staticmethod:: ctcl__platform(commandbody)
    
        This method is to change Command Dict Object into :py:class:`pwbs.command.command.Platform`.

        :argument dict commandbody: Command Dict Object
    
        