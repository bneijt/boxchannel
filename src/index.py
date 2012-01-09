#!/usr/bin/python
import boxchannel
import simplejson as json
import random
import os
import sys

def loadUserPreferences():
    fname = os.path.expanduser("~/.boxchannel.json")
    if not os.path.exists(fname):
        return json.loads("{}")
    maximumPreferencesFileSize = 1024*1024
    return json.loads(file(fname).read(maximumPreferencesFileSize))

def saveUserPreferences(prefs):
    fname = os.path.expanduser("~/.boxchannel.json")
    file(fname, 'w').write(json.dumps(prefs))

def main():
    #Load or generate user preferences
    prefs = loadUserPreferences()
    if 'id' not in prefs:
        prefs['id'] = str(random.random())[2:]
        saveUserPreferences(prefs)
        print "New user id: ", prefs['id']
    indexFile = file("%s.index" % prefs['id'], 'w')
    for fileName in sys.argv[1:]:
        print "Indexing ", fileName
        newFile = file(fileName, 'r')
        indexFile.write(os.path.abspath(fileName))
        for blockHash in boxchannel.hashesFor(newFile):
            indexFile.write(" %s" % blockHash)
        indexFile.write("\n")
    indexFile.close()

if __name__ == "__main__":
    main()
