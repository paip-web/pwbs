PAiP Web Build System
=====================

Actual Version : **v.0.5.0-dev0**

**PWBS** is Build System for easy automation process.


* Licensed under MIT License
    *
        .. image:: https://img.shields.io/pypi/l/pwbs.svg
            :target: https://gitlab.com/paip-web/pwbs/blob/master/LICENSE
* PyPi Package: https://pypi.org/project/pwbs/
    *
        .. image:: https://img.shields.io/pypi/v/pwbs.svg
            :target: https://pypi.org/project/pwbs/
    *
        .. image:: https://badge.fury.io/py/pwbs.svg
            :target: https://badge.fury.io/py/pwbs
    *
        .. image:: https://img.shields.io/pypi/status/pwbs.svg
    *
        .. image:: https://img.shields.io/pypi/format/pwbs.svg
    *
        .. image:: https://img.shields.io/pypi/implementation/pwbs.svg
        .. image:: https://img.shields.io/pypi/pyversions/pwbs.svg
* Documentation on **readthedocs.io**
    *
        .. image:: https://readthedocs.org/projects/pwbs/badge/?version=latest
            :target: http://pwbs.readthedocs.io/en/latest/?badge=latest

Features
--------

Current Features
~~~~~~~~~~~~~~~~

* Single Tasks
    Task executes one command
* Multi Command Tasks
    Task executes multiple commands

Planned Features
~~~~~~~~~~~~~~~~

* Multi Task
    Tasks that executes other tasks
* Watcher Task
    Task that executes command or task when something in watched path changes
* Scheduler Task
    Task that executes command or task every X time
* Server Mode Task
    Task that makes simple HTTP Server that listens for request
    and on request executes specified tasks or commands
* WebSocket Server Mode
    Mode that makes PWBS create WebSocket Server listenning tasks to execute
* Web Interface Server Mode
    Mode that makes HTTP Server that serves simple Web Interface
    for executing tasks through it

Credits
---------

Created by **Patryk Adamczyk**
