Boxchannel
==========

Introduction
------------
The idea of boxchannel is to have a network shared directory where two boxchannel agents can set up a communication channel with each other. Allowing you to share large amounts of data.


Overview
--------
A boxchannel channel is a directory containing the following subdirectories:
request
response


If a deamon can fulfill a request, it will remove the file form the request directory and place the data in the response directory.

Cleaning up
===========
Requests
--------
Each request is a json file, whith an issued timestamp.
All daemons are required to remove requests older then 2 days.

Responses
---------
All responses have the format: sha1.timestamp
Timestamp is the time the file was added.
All daemons are required to remove requests older then 2 days
All daemons are required to remove the oldest entry while there are more then 200 entries in the channel.




