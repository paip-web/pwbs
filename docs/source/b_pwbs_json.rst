============================
pwbs.json Configuration File
============================

*****
Tasks
*****

Single Task
===========

Reimplemented in v.0.4.0dev0

Description ::

    Maps task name to one command.

    When you run this task you execute exactly one command which specified.

Example ``pwbs.json`` ::

    {
        "commands" : {
            "task" : "command"
        }
    }

Example Description ::

    task - Task Name
    command - Command which you want to run when you run this task

MultiCommand Task
=================

Reimplemented in v.0.4.0dev0

Description ::

    Maps task name to commands.

    When you run this task you execute all commands which you specified you want to run with this task.

Example ``pwbs.json`` ::
    
    {
        "commands" : {
            "task" : {
                "mode" : "mc",
                "commands" : [
                    "command1",
                    "command2"
                ]
            }
        }
    }

Example Description ::

    task - Task Name
    command1, command2 - Command which you want to run when you run this task [For sure you can to specify more than 2]


Multi Task
==========

Not implemented in v.0.4.0dev0

Description ::

    Maps task name to other tasks.

    When you run this task you execute commands from the tasks you specified.


Example ``pwbs.json`` ::

    {
        "commands" : {
            "task" : [
                "task1",
                "task2"
            ]
        }
    }

Example Description ::

    task - Task Name
    task1, task2 - Tasks which you want to run when you run this task [For sure you can to specify more than 2]


Watcher
=======

Not implemented in v.0.4.0dev0

Description ::

    Maps task name to watcher task.

    When you run this task it waits (or execute commands and waits) for changes in specified directories and after change it executes commands.


Example ``pwbs.json`` ::

    {
        "commands" : {
            "task-1" : {
                "mode" : "wc0",
                "context" : [
                    "path/to/watch/*"
                ],
                "commands" : [
                    "command1"
                ]
            },
            "task-2" : {
                "mode" : "wc",
                "context" : [
                    "path/to/watch/*"
                ],
                "commands" : [
                    "command1"
                ]
            }
        }
    }

Example Description ::

    task-1 is example of the Run, Execute, Watch Task
    task-2 is example of the Run, Watch Task

    task-1, task-2 - Task Name
    path/to/watch/* - Path you want to watch [You can specify more than one]
    command1 - Commands you want to execute when context is changed


Scheduler
=========

Not implemented in v.0.4.0dev0

Description ::

    Maps task name to scheduler task.

    When you run this task it waits (or execute commands and waits) until every specified time.

Example ``pwbs.json`` ::

    {
        "commands" : {
            "task-1" : {
                "mode" : "s0",
                "context" : 00000000000,
                "commands" : [
                    "command1"
                ]
            },
            "task-2" : {
                "mode" : "s",
                "context" : 00000000000,
                "commands" : [
                    "command1"
                ]
            }
        }
    }

Example Description ::

    task-1 is example of the Run, Execute, Wait Task
    task-2 is example of the Run, Wait Task

    task-1, task-2 - Task Name
    00000000000 - Time you want to wait until execute [Time specify in seconds] [You can specify more time than one]
    command1 - Commands you want to execute when context is changed


************
JSON Schemas
************

PWBS Local Configuration File [It's schemas with not implemented features too]



* `PWBS_LCF-pwbs.json Working Draft <https://gitlab.com/paip-web/pwbs/raw/develop/docs/source/schema/PWBS_LCF_WD.json>`_

    .. literalinclude:: schema/PWBS_LCF_WD.json

* `PWBS_LCF-pwbs.json v.0.3 <https://gitlab.com/paip-web/pwbs/raw/develop/docs/source/schema/PWBS_LCF_v_0_3.json>`_

    .. literalinclude:: schema/PWBS_LCF_v_0_3.json

* `PWBS_LCF-pwbs.json v.0.2 <https://gitlab.com/paip-web/pwbs/raw/develop/docs/source/schema/PWBS_LCF_v_0_2.json>`_

    .. literalinclude:: schema/PWBS_LCF_v_0_2.json

* `PWBS_LCF-commands.json v.0.1 <https://gitlab.com/paip-web/pwbs/raw/develop/docs/source/schema/PWBS_LCF_v_0_1.json>`_

    .. literalinclude:: schema/PWBS_LCF_v_0_1.json


*******************************************
**FUTURE:** Full PWBS pwbs.json Config File
*******************************************

Not implemented [additional features] in any way in v.0.4.0dev0

Full Example ``pwbs.json`` ::

    /* PWBS Local Configuration File 
    * pwbs.json
    * PWBS_LCF-pwbs.json v.0.3
    */
    {
        "config" : {
            "settings" : {
                "json-plugins" : true,                  // Enabling JSON Plugins [Default False]
                "py-plugins" : true,                    // Enabling Python Plugins [Default False]
                "verbose-mode" : 255,                   // Changing Verbose Mode [Default 1] (This setting can be overwrited in the run of pwbs by the --verbose flag)
                "os-tasks" : true,                      // Enabling Operating System Specific Tasks [Default False]
                "debug-mode" : true,                    // Enabling Debug Mode [Default False] (This setting can be overwrited in the run of pwbs by the --debug flag)
                "test-mode" : true,                     // Enabling Test Mode [Default False] (This setting can be overwrited in the run of pwbs by the --test-mode flag)
                "pwbs-integrated-tasks" : true,         // Enabling PWBS Integrated Tasks [Default False]
                "pwbs-integrated-plugins" : true,       // Enabling PWBS Integrated Plugins [Default False]
                "lcf-plugins" : true                    // Enabling PWBS Local Configuration File - Plugins [Default False] (This option is like importing tasks from another pwbs.json)
            },
            "use" : {
                "py-plugins" : [ // Python Plugins
                    "coffeescript",
                    "stylus",
                    "concatenate",
                    "git"
                ],
                "json-plugins" : [ // JSON Plugins
                    "test"
                ],
                "lcf-plugins" : [ // Local Configuration File - Plugins
                    "test.pwbs.json"
                ]
            }
        },
        "commands" : {
            "deps-install" : {
                "mode" : "st", // Single Task
                "commands" : { // Commands
                    "windows" : { // Commands for Windows
                        "pip install -r requirements.txt"
                    },
                    "other" : { // Commands for everything else
                        "pip3 install -r requirements.txt"
                    }
                },
                "comment" : "Installs Dependencies" // Comment
            },
            "compile" : {
                "mode" : "wc0", // Watcher Task
                "context" : [ // Watcher Context
                    "website/blog/static/blog/stylus",
                    "website/blog/static/blog/coffee"
                ],
                "comment" : "Compiling your files to normal static files.", // Comment
                "arg" : { // Arguments to be used in this task (used from template language)
                    "tmpdir" : "compiled_tmpdir",
                    "compileddir" : "website/blog/static/blog/res"
                },
                "commands" : [
                    { // Argumented Task
                        "task" : "--git--add",
                        "args" : [
                            "all"
                        ]
                    },
                    {
                        "task" : "--git--commit",
                        "args" : [
                            {
                                "message" : "$(%tl->>date('d-m-Y H:M:s')) - PWBS Auto Compiler Task" // Argument with template language interpolatation
                            }
                        ]
                    }
                    "--coffeescript--init", // Normal task
                    "--stylus--init",
                    {
                        "task" : "--coffeescript--compile",
                        "args" : [
                            "$(%this->>context)", // Argument with template language interpolation using task arguments and task context
                            "$(%this->>arg->tmpdir)",
                            [
                                "bare",
                                "map"
                            ]
                        ]
                    },
                    {
                        "task" : "--stylus--compile",
                        "args" : [
                            "$(%this->>context)",
                            "$(%this->>arg->tmpdir)",
                            [
                                "compress",
                                "map",
                                "autoprefix"
                            ]
                        ]
                    },
                    {
                        "task" : "--concatenate--compile",
                        "args" : [
                            "$(%this->>arg->tmpdir)",
                            "$(%this->>arg->compileddir)",
                            [
                                "main.css",
                                "main.js"
                            ]
                        ]
                    },
                    "--test--testcompiled",
                    "--lcf--cleanup"
                ]
            }
        }
    }