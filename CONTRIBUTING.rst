==================
Contribution Guide
==================

*********************************
Welcome in our Contribution Guide
*********************************

Contributions are welcome, and they are greatly appreciated!

Every little bit helps a lot, and credit will always be given.

*********************
How can i contribute?
*********************

You can contribute and help in many ways.

Types of Contributions
======================

Submit Feedback
---------------

The best way to send feedback is to file an issue at https://gitlab.com/paip-web/pwbs/issues .

Issue template is in another section of that document.

If you are proposing a feature explain in detail how it would work.

Write Documentation
-------------------

PWBS (PAiP Web Build System) could always use more documentation and always can have better constructed documentation. Whether as part of official PWBS docs, in docstrings, or even on the web in blog posts, articles, and such.

If you find mistyped word then file an issue or change and submit merge request.

Report Bugs
-----------

Report bugs at https://gitlab.com/paip-web/pwbs/issues .

Issue template is in another section of that document.

If you are reporting a bug, please include:

* Your operating system name and version

* Any details about your local setup that might be helpful in troubleshooting.

* Detailed steps to reproduce bug.

Fix Bugs
--------

Look through the GitLab issues for bugs. Anything tagged with "bug" is open to whoever wants to implement it.

Implement Features
------------------

Look through the Roadmap in documentation and check what wasn't done. Everything what will be there is open to whoever wants to implement it.

********************************
Rules and Additional Information
********************************

Rules
=====

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.

2. Add your changes to ChangeLogs
    
    * docs/source/n_changelog.rst (Every even small change)

    * HISTORY.rst (For every big change in functionality)

3. The pull request should work for Python >= 3.6 and be OS independent.

Tests
-----

To run tests run any of these:

* ``pytest``

* ``pwbs --run-tests``

* ``python -m pwbs --run-tests``

If you make tests keep ordering don't fillout missing numbers.
Last Documented Test is 5? Then make test 6 not 4 because it's missing number.

Templates
=========

Feedback Issue Template
-----------------------

There where in this template is <Something> that means your data.

Issue ::

    Title | Feedback: <Name or Nick>
    Description | <Your Feedback and/or Your Feature Proposal>
    Milestone | NEXT
    Label | FEEDBACK

Bug Report Issue Template
-------------------------

There where in this template is <Something> that means your data.

Issue ::

    Title | BUG: <Name of Bug>
    Description | <Your Information about the bug>
    Milestone | BUG
    Label | BUG




