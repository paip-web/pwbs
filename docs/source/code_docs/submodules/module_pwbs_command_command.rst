pwbs.command.command
--------------------

.. py:module:: pwbs.command.command

This module is place for main PWBS Program Class.

.. py:class:: CommandType()

    This class is Enum of Task Types.

    .. py:attribute:: NullTask = 0x000

        This type is Null Task (Special type to make null type task).
    
    .. py:attribute:: InitialNullTask = 0x001
    
        This type is Null Task type that are used to initialize CommandType Object in Command Class.
    
    .. py:attribute:: SpecialTask = 0x101
    
        This type is Special Task type.

    .. py:attribute:: SingleTask = 0x201
    
        This type is Single Task type.

    .. py:attribute:: MultiTask = 0x202
    
        This type is Multi Task type.

    .. py:attribute:: MultiCommandTask = 0x203
    
        This type is Multi Command Task type.
    
    .. py:attribute:: WatcherTask = 0x204
    
        This type is Watcher Task type. [FUTURE:]

    .. py:attribute:: SchedulerTask = 0x205
    
        This type is Scheduler Task type. [FUTURE:]

    .. py:attribute:: TestTask = 0xFF0
    
        This type is Test Task type. This type is for tests only.

    .. py:attribute:: ErrorTask = 0xFF1
    
        This type is Error Task type. This type is for error catching purposes.

    .. py:attribute:: NullTaskF = 0xFFF
    
        This type is Null Task type (Special type for make null task).

.. py:class:: Platform()

    This class is for making specific platform tasks. [FUTURE:]

    .. py:attribute:: NullOS = 0b0000
    
        This is for no platform.

    .. py:attribute:: Windows = 0b0001
    
        This is for Windows platform.

    .. py:attribute:: Linux = 0b0010
    
        This is for Linux platform.

    .. py:attribute:: MacOS = 0b0100
    
        This is for Mac OS X platform.
    
    .. py:attribute:: Other = 0b1000
    
        This is for other platforms.
    
    .. py:attribute:: Any = 0b1111
    
        This is for any platform.

.. py:class:: CommandMode()

    This class is for Tasks Modes.

    .. py:attribute:: SingleTask_Standard = 0x2201001
    
        This is Single Task - Standard Mode.

    .. py:attribute:: MultiTask_Standard = 0x2202001
    
        This is Multi Task - Standard Mode.

    .. py:attribute:: MultiCommandTask_Standard = 0x22030001
    
        This is Multi Command Task - Standard Mode
    
    .. py:attribute:: WatcherTask_StartAndRun = 0x22040001
    
        This is Watcher Task - Start, Run Commands and Wait Mode.
    
    .. py:attribute:: WatcherTask_StartAndWait = 0x22040002
    
        This is Watcher Task - Start and Wait Mode.
    
    .. py:attribute:: Scheduler_StartAndRun = 0x22050001
    
        This is Scheduler Task - Start, Run Commands and Wait Mode.
    
    .. py:attribute:: Scheduler_StartAndWait = 0x22050002
    
        This is Scheduler Task - Start and Wait Mode.

    .. py:attribute:: NullMode = 0x00000000
    
        This is null mode.
    
    .. py:attribute:: ModeNotSpecified = 0x00000001
    
        This is Mode for not specified mode.

    .. py:attribute:: TestTask_TestMode = 0xFFF00000
    
        This is Test Task - Test Mode.
    
    .. py:attribute:: ErrorTask_ErrorMode = 0xFFF1FFFF
    
        This is Error Task - Error Mode.

    .. py:attribute:: NullTask_NullMode = 0xF000FFF0
    
        This is Null Task - Null Mode.
        
    .. py:attribute:: NullTaskF_NullMode = 0xFFFFFFF0
    
        This is Null Task F - Null Mode.

    .. py:attribute:: ErrorMode = 0xFFFFFFFF
    
        This is Error Mode.

.. py:class:: Command(name, cmd_type: CommandType = CommandType.InitialNullTask, commands: list = None, comment: str = "", mode: CommandMode = CommandMode.NullMode, arguments: dict = None, special: dict = None, platform: Platform = Platform:Any) -> None

    This is Command Class. It's used to make Tasks from JSON to Python object. 

    Constructor making this steps:

    * Making Logger Object

    * Defining Variables

    :argument str name: Name of the Command (Task).

    :argument CommandType cmd_type: Type of Command.
    
        Default it's set to :py:attr:`pwbs.command.command.CommandType.InitialNullTask`.

    :argument list commands: List of Commands.
    
        Default it's set to :py:class:`None`.

    :argument CommandMode mode: Mode of Command (Task).
    
        Default it's set to :py:attr:`pwbs.command.command.CommandMode.NullMode`.

    :argument dict arguments: Arguments of Command (Task).
    
        Default it's set to :py:class:`None`.

    :argument dict special: Special Arguments of Commands (Task).
    
        Default it's set to :py:class:`None`.

    :argument Platform platform: Platform of Command (Task).
    
        Default it's set to :py:attr:`pwbs.command.command.Platform.Any`

    :return: :py:class:`None`
    :rtype: :py:class:`None`

    .. py:attribute:: _log = pwbs.log.logger.Logger()
    
        Logger Object
    
    .. py:attribute:: name
    
        Name of Command

    .. py:attribute:: type
    
        Type of Command

    .. py:attribute:: commands
    
        Commands specified to execute when task is called.

    .. py:attribute:: comment
    
        Comment to Command

    .. py:attribute:: mode
    
        Mode of Command

    .. py:attribute:: arguments
    
        Arguments of Command

    .. py:attribute:: special
    
        Special Arguments of the Command

    .. py:attribute:: platform
    
        Platform for the Command

    .. py:method:: __eq__(self, other)
    
        This thunder method is for Equation Operator Overload for this class.

    .. py:method:: run()
    
        This method is used to run task and commands associated with it.

        TODO: MultiTask

        :raises Exception: Error Task Reached. [TODO: Change exception]
        :raises NotImplementedError: If not supported task type is reached.
        :return: None
        :rtype: None

        This method is making these steps:

        * Checking type

        * Running Special ``execute_as_XXXXXXX()`` method for specified type

    .. py:method:: execute_as_singletask_or_multicommand()
    
        This method is executing that Command object as SingleTask or MultiCommandTask.

        .. py:function:: prefixer(text)
        
            Text Prefixer needed for that function. Used to time command outputs.

            :param str text: Text to prefix
    
    .. py:method:: execute_as_watcher()
    
        :raises NotImplementedError: Feature not Implemented! [TODO:]
    
    .. py:method:: execute_as_scheduler()
    
        :raises NotImplementedError: Feature not Implemented! [TODO:]

    .. py:method:: __add__(self, other)
    
        This thunder method is for Adding Operator Overload for this class.

    .. py:method:: argument_parser()
    
        This method is for argument_parser.

        :return: :py:attr:`pwbs.command.command.Command.comment`
        :rtype: :py:class:`str`

.. py:class:: CommandList(value: Command) -> None

    This class is for making list Commands Class Objects.

    :argument Command value: Array of values [Type: List of Command Class Objects]
    :return: None
    :rtype: None

    .. py:attribute:: values
    
        Values of the CommandList

    .. py:method:: __getitem__(self, key)
    
        This thunder method is for X[Y] Operator Overload for this class.

    .. py:method:: __setitem__(self, key, value)
    
        This thunder method is for X[Y] = Z Operator Overload for this class.

    .. py:method:: __delitem__(self, key)
    
        This thunder method is for del X[Y] Operator Overload for this class.

    .. py:method:: __contains__(self, item)
    
        This thunder method is for Y in X Operator Overload for this class.

    .. py:method:: items()
    
        This method returns all items in CommandList.

        :return: :py:attr:`pwbs.command.command.CommandList.values`
        :rtype: :py:class:`list`