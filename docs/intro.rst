============
Introduction
============

About
=====

Place holder for Intro section
This document provides a set of best practices for open source contributions -
bug reports, code submissions / pull requests, etc.

For the most part, these guidelines apply equally to *any* project regardless
of programming language or topic. Where applicable, we outline where individual
projects/languages may have additional requirements.

Naturally, this document is itself open source, and we encourage feedback &
suggestions for improvement.

Sources
-------

Currently this document draws from the contribution documentation for a handful
of related Python open source projects: `Fabric <http://fabfile.org>`_, `Invoke
<http://pyinvoke.org>`_, `Paramiko <http://paramiko.org>`_, etc.

It's expected that over time we will incorporate additional material from
related attempts at consolidating this type of info. We'll update with a list
here when that happens.


Submitting bugs
===============

Due diligence
-------------

Before submitting a bug, please do the following:

* Perform **basic troubleshooting** steps:

    * **Make sure you're on the latest version.** If you're not on the most
      recent version, your problem may have been solved already! Upgrading is
      always the best first step.
    * **Try older versions.** If you're already *on* the latest release, try
      rolling back a few minor versions (e.g. if on 1.7, try 1.5 or 1.6) and
      see if the problem goes away. This will help the devs narrow down when
      the problem first arose in the commit log.
    * **Try switching up dependency versions.** If the software in question has
      dependencies (other libraries, etc) try upgrading/downgrading those as
      well.

* **Search the project's bug/issue tracker** to make sure it's not a known
  issue.
* If you don't find a pre-existing issue, consider **checking with the mailing
  list and/or IRC channel** in case the problem is non-bug-related.