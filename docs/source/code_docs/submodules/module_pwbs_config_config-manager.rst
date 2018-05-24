pwbs.config.config_manager
--------------------------

.. py:module:: pwbs.config.config_manager

This module is place for Configuration Manager.

.. py:exception:: PWBSConfigFileDontExistError

    Exception for handling ``Local Config File Don't Exist``

.. py:exception:: PWBSInvalidConfigFile

    Exception for handling ``Invalid Format of Local Config File``

.. py:class:: ConfigManager(filename="pwbs.json")

    This class is for Managing Configuration File.

    :argument str filename: Filename of Configuration File.

        Defaults to ``pwbs.json``.

    :raises PWBSConfigFileDontExistError: Local Configuration File Don't Exist

    .. py:attribute:: config_filename
    
        Configuration File Filename

    .. py:attribute:: config_filename_path
    
        Configuration File Path
    
    .. py:attribute:: error = None
    
        Variable contains errors when they occur.

    .. py:attribute:: filemanager = pwbs.lib.pwm.pwm_json.JSON_IO(self.config_filename_path)
    
        File Manager Object

    .. py:attribute:: config_dict
    
        Configuration File Dictionary Object

    .. py:method:: load()
    
        This method is trying to load Configuration File Data.

        :return: :py:attr:`pwbs.config.config_manager.ConfigManager.config_dict`
        :rtype: :py:class:`dict`
        :raises PWBSInvalidConfigFile: If in Configuration File doesn't exist commands key (Which means that config file is invalid).

    .. py:method:: write(newdata)
    
        This method is overwriting Configuration File with new data.

        :return: New data provided but returned from writing and reading config file.
        :rtype: :py:class:`dict`