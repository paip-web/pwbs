==============
PWBS CLI Usage
==============


**********
Quickstart
**********

1. Install Python 3 [>3.5]

2. Install PWBS [``pip install pwbs`` OR ``pip3 install pwbs`` (Platform Depending)]

3. Go to your project where you want to use pwbs

4. Create ``pwbs.json`` file [FUTURE: ``pwbs --new-config``]

5. Create in that file that structure::

    {
        "commands" : {
        }
    }

6. Add your tasks to ``pwbs.json`` file [Just add normal json key:value pair where key is taskname and value is command]
7. Run you tasks ``pwbs <task>``

****************************
Full CLI Usage Documentation
****************************

.. program:: pwbs

Help
====

.. option:: -h, -help

    Show help message and exit

Special Tasks
=============

.. option:: -v {0,1,2,3,255}, --verbose {0,1,2,3,255}

    Changing Verbosity

    0. No Information about running

    1. Normal Information about running [Default Level]

    2. More Information about running

    3. More Information about running and work behind the scenes

    255. Debug Verbosity Mode

.. option:: --debug

    Debug Mode

    Debug Mode is turned off by default.

.. option:: --version

    Showing Version of PWBS

.. option:: --new-config

    [FUTURE:]

    Creating Blank Configuration File from basic template

.. option:: -l, --log

    Enabling Active Logging

.. option:: -lf LOGFILE, --logfile LOGFILE, --log-file LOGFILE

    Specifying Log File

    Default Log File: ./pwbs.log

.. option:: -c CONFIGFILE, --configfile CONFIGFILE, --config-file CONFIGFILE

    Specifying Configuration File

    Default Configuration File: ./pwbs.json

.. option:: --test-mode

    Enabling Test Mode

    What it doing behind the scenes?
    Changing Verbosity to: 255.
    Changing to Debug Mode.

.. option:: --run-tests

    Starting PWBS Test Runner

Tasks
=====

.. option:: TASK

    Task to be executed