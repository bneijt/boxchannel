Boxchannel
==========

Introduction
============
The idea of boxchannel is to have a network shared directory where two boxchannel agents can set up a communication channel with each other. Allowing you to share large amounts of data over a fixed size shared directory.

Project goal: Point a GUI to a Dropbox directory you share with friend and have it manage downloads and uploads while keeping the total directory size under (say) 200MB.

Current scripts
====================

BEWARE: All these scripts will create files, including `~/.boxchannel.json` and directories and files in your `~/Dropbox` directory. These scripts are currently for DEVELOPERS ONLY.

index.py
--------
Add files to your index. Index files are currently in `~/Dropbox/boxchannel/_userid_.index`
Each line is a absolute path followed by each of the block hashes. The _userid_ is a random
number generated if there is no `~/.boxchannel/prefs.json` file with an id in it.

boxchannel.py
-------------
Currently the library containing all logic, a big box of all functions.

respond.py
----------
For each request, see if our local index has a block for it, then publish the block and remove the request.

request.py
----------
Given a filename, search all index databases for that file and when found, request all blocks of the file.

boostrap.sh
-----------
Use `virtualenv` to create a python environment and install mmh3.

stage.py
--------
TODO: collect all request we made (empty files in staging area) and try to fill them with data. As soon as we have a full file, collect the staged block and dump them.

TODO list
=========

*   Create stage.py
*   Add clean up scripts
*   Add unit tests
*   Refactor boxchannel into a real kind of library
*   Add `--append` support to index.py to allow you to write `find . -type f -print0|xargs -0 -P1 -n1000 index.py --append`
*   Add `--help` support to all scripts




