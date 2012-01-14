#!/usr/bin/python
import mmh3
import glob
import binascii
import sys
import logging
import hashlib
import simplejson as json
import random
import os
import sys

blockSize = 1024*1024*10
preferencesFileName = os.path.expanduser("~/.boxchannel/preferences.json")

class LocalBlock:
    def __init__(self, filename, index):
        self._index = index
        self._filename = filename


def blockHash(block):
    hashBytes = mmh3.hash_bytes(block)
    return binascii.hexlify(hashBytes)


def hashesFor(f):
    while True:
        data = f.read(blockSize)
        if len(data) == 0:
            break
        yield blockHash(data)

def publishBlock(blockInfo):
    logging.log("publishing: %s", blockInfo)
    

def loadUserPreferences():
    fname = preferencesFileName
    if not os.path.exists(fname):
        return json.loads("{}")
    maximumPreferencesFileSize = 1024*1024
    return json.loads(file(fname, 'r').read(maximumPreferencesFileSize))

def indexedFiles(indexFileDirectory):
    for indexFileName in glob.glob(os.path.join(indexFileDirectory, "*.index")):
        indexFile = file(indexFileName, 'r')
        for line in indexFile.xreadlines():
            yield line.split(" || ", 1)


def initUserPreferences():
    prefs = loadUserPreferences()
    needToSave = False
    if 'id' not in prefs:
        prefs['id'] = str(random.random())[2:]
        needToSave = True
        print "New user id: ", prefs['id']
    if 'indexDirectory' not in prefs:
        prefs['indexDirectory'] = os.path.expanduser("~/Dropbox/boxchannel/")
        needToSave = True
    if 'requestDirectory' not in prefs:
        prefs['requestDirectory'] = os.path.expanduser("~/Dropbox/boxchannel/request")
        needToSave = True
    if 'responseDirectory' not in prefs:
        prefs['responseDirectory'] = os.path.expanduser("~/Dropbox/boxchannel/response")
        needToSave = True
    if 'stageDirectory' not in prefs:
        prefs['stageDirectory'] = os.path.expanduser("~/.boxchannel/stage")
        needToSave = True
    if 'downloadDirectory' not in prefs:
        prefs['downloadDirectory'] = os.path.expanduser("~/Downloads")
        needToSave = True
    
    if needToSave:    
        saveUserPreferences(prefs)
    return prefs    

def saveUserPreferences(prefs):
    fname = preferencesFileName
    pf = file(fname, 'w')
    pf.write(json.dumps(prefs))
    pf.close()


