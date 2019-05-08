Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog
<https://keepachangelog.com/en/1.0.0/>`_
with additional group for informations,
and this project adheres to `Semantic Versioning
<https://semver.org/spec/v2.0.0.html>`_.

[Unreleased]
------------

.. Informations
.. ^^^^^^^^^^^^
.. - `Release 11 (pwbs 0.5.0.dev0) <https://pypi.org/project/pwbs/0.5.0.dev0/>`_

Added
^^^^^
- Sentry Error Tracking
- Help on run without arguments
- PWBS Event Manager
- [Schema] PWBS Local Configuration File Schema Version v.0.4

Changed
^^^^^^^
- Changelog Format
- Absolute Imports
- Documentation Rephrase

Deprecated
^^^^^^^^^^
- PWM (To change into internal functions or pwm as dependency)
- PWBS (Old version of PWBS runnning automation tasks for semantic versioning)

Removed
^^^^^^^

Fixed
^^^^^
- Code Style

[0.4.0-alpha0] - 2018-09-25
---------------------------

Informations
^^^^^^^^^^^^
- `Release 10 (pwbs 0.4.0a0) <https://pypi.org/project/pwbs/0.4.0a0/>`_
- Release for blocking stable on Alpha Release

[0.4.0-dev0] - 2018-09-25
-------------------------

Informations
^^^^^^^^^^^^
- `Release 9 (pwbs 0.4.0.dev0) <https://pypi.org/project/pwbs/0.4.0.dev0/>`_
- Complete Rewrite of PWBS

Added
^^^^^
- **[PWBS Functionality] Single Tasking**
- **[PWBS Functionality] Multi Command Tasking**
- CLI Argument Parsing using `argparse`
- PWBS Config Manager
- PWBS Logger
-
    [PWBS CLI] Special Command `--verbose`
    (Set Verbose Level [Possible: 0, 1, 2, 3, 255]
-
    [PWBS CLI] Special Commnad `--debug`
    (Turn on Debug Mode)
-
    [PWBS CLI] Special Command `--version`
    (Show version of PWBS)
-
    [PWBS CLI] Special Commnad `--new-config`
    (Generate new configuration file)
-
    [PWBS CLI] Special Command `--log`
    (Turning on logging to file)
-
    [PWBS CLI] Special Command `--logfile`
    (File to log onto)
-
    [PWBS CLI] Special Commnad `--configfile`
    (File to load as configuration file)
-
    [PWBS CLI] Special Command `--test-mode`
    (Special Test Mode (V: 255, Debug: on))
-
    [PWBS CLI] Special Command `--run-tests`
    (Run PWBS Testing Module)
- Tests for PWBS
- Loggers -> LoggerAssertionError
- Loggers -> Base Logger (Handling logging to console)
- Loggers -> Log Logger (Handling logging to file)
- Loggers -> Logger (Handling Logging to file and console)
- Config -> PWBSConfigFileDontExistError
- Config -> PWBSInvalidConfigFile
- Config -> Config Manager
- Config -> PWBS Config Manager
- Command -> Command Type Enum
- Command -> Command Platform Enum
- Command -> Command Mode Enum
- Command -> Command Class
- Command -> Commnad List Class [Command Collection]
- Full Documentation in RST using Sphinx
- [Schema] PWBS Local Configuration File Schema Version v.0.1
- [Schema] PWBS Local Configuration File Schema Version v.0.2
- [Schema] PWBS Local Configuration File Schema Version v.0.3
- [Schema] PWBS Local Configuration File Schema Version Working Draft
- Configuration to host documentation on ReadTheDocs

Changed
^^^^^^^
- Moved PWM to `lib/pwm`

Removed
^^^^^^^
- **[PWBS Functionality] Multi Tasking**
- Task Interpreter
- Special Commands Interpreter
- Commands Interpreter
- PWBS Utilities Functions
- Tests
- Documentation

[0.3.0-dev1] - 2017-12-22
-------------------------

Informations
^^^^^^^^^^^^
- `Release 8 (pwbs 0.3.0.dev1) <https://pypi.org/project/pwbs/0.3.0.dev1/>`_

Added
^^^^^
- Task Interpreter - Support for Multi Task

[0.2.0-dev3] - 2017-12-20
-------------------------

Informations
^^^^^^^^^^^^
- Not Released on PyPi (Eventually it's not on in Release History)

Changed
^^^^^^^
- [PWM] Tests for PWM to check is Modules reads files correctly on whatever OS

Fixed
^^^^^
- File Path Errors (By base on Windows)

[0.2.0-dev2] - 2017-12-16
-------------------------

Informations
^^^^^^^^^^^^
- `Release 7 (pwbs 0.2.0.dev2) <https://pypi.org/project/pwbs/0.2.0.dev2/>`_

Fixed
^^^^^
- Description Files

[0.2.0-dev1] - 2017-12-16
-------------------------

Informations
^^^^^^^^^^^^
- `Release 6 (pwbs 0.2.0.dev1) <https://pypi.org/project/pwbs/0.2.0.dev1/>`_

Added
^^^^^
- Task Interpreter
- Task Interpreter - Support for Single Tasks
- Command Interpreter -> Normal Task Interpreter
- [PWM] [pwm_exec] Execute Generator Function

[0.1.0-dev2] - 2017-12-16
-------------------------

Informations
^^^^^^^^^^^^
- `Release 5 (pwbs 0.1.0.dev2) <https://pypi.org/project/pwbs/0.1.0.dev2/>`_

Added
^^^^^
- [PWBS CLI] Special Command --new-config
- [PWBS CLI] Special Command --config <file>
- PWBS Config Manager for loading Configuration File

[0.1.0-dev1] - 2017-12-13
-------------------------

Informations
^^^^^^^^^^^^
- `Release 4 (pwbs 0.1.0.dev1) <https://pypi.org/project/pwbs/0.1.0.dev1/>`_

Added
^^^^^
- Documentation Base
- Test for PWBS Module
- [PWM] Tests for PAiP Web Modules

Fixed
^^^^^
- Package Description

[0.0.1-dev4] - 2017-12-12
-------------------------

Informations
^^^^^^^^^^^^
- `Release 3 (pwbs 0.0.1.dev4) <https://pypi.org/project/pwbs/0.0.1.dev4/>`_

Added
^^^^^
- AUTHORS File
- Contribution Guide
- Error List
- PWBS Command Interpreter
- [PWBS CLI] Special Command --help
- [PWBS CLI] Special Command --verbose <mode>
- Tox as Test Runner for Python Versions Testing
- Changed Python Required Minimum Version to Python 3.5
- Changed encoding to open files that are part of description to UTF-8

[0.0.1-dev3] - 2017-12-09
-------------------------

Informations
^^^^^^^^^^^^
- `Release 2 (pwbs 0.0.1.dev3) <https://pypi.org/project/pwbs/0.0.1.dev3/>`_

Added
^^^^^
- Full Baner with Debug Information in verbose modes [PWBS CLI]
- Description for Package on PyPi
- Basic Test for PWBS


[0.0.1-dev2] - 2017-12-09
-------------------------

Informations
^^^^^^^^^^^^
- First Release on PyPi
- `Release 1 (pwbs 0.0.1.dev2) <https://pypi.org/project/pwbs/0.0.1.dev2/>`_

Changed
^^^^^^^
- README File
- Ready To Release Improvements

[0.0.1-dev1] - 2017-12-09
-------------------------

Informations
^^^^^^^^^^^^
- PAiP Web Modules
    -
        It's was an idea as simple modules which act
        like little libraries for specific things
    -
        From this version on PWM was little library
        writed in pwbs as internal dependency

Added
^^^^^
- Setup Configuration for Release to PyPi
- PyLint Configuration
- Coverage Configuration
- First Version of Changelog
- PAiP Web Modules
- PWM - Debug
- PWM - Execution
- PWM - JSON
- PWM - System Information
- PWM - Watcher
- Basic Baner in PWBS CLI

[0.0.0-dev5] - 2017-12-08
-------------------------

Changed
^^^^^^^
- Version Change for checking bumpversion configuration

[0.0.0-dev4] - 2017-12-08
-------------------------

Added
^^^^^
- Tests for checking is Python working correctly
- Started working on base Python Module

[0.0.0-dev3] - 2017-12-08
-------------------------

Informations
^^^^^^^^^^^^
- First Commit on GitLab Repository of PWBS Project

Added
^^^^^
- PAiP Web Build System Edition 1 - v.0.9.1.0
- GitLab Repository for Project
- Base requirements file
- Base version of PWBS is used for automation of development of new one
- Bumpversion Configuration for Semantic Versioning Tooling
- CI Python Script [For Continuos Testing in Local Development Environment[

[0.0.0] - 2017-12-08
--------------------

Informations
^^^^^^^^^^^^
- Actual Versions of PWBS are based on single file implementation of pwbs ideas
- These Version of PWBS starts work on PAiP Web Build System Edition 2 Project

Added
^^^^^
- PAiP Web Build System Edition 1 - v.0.9.1.0
