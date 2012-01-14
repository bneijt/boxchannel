#!/usr/bin/python
import boxchannel
import os
import sys
import simplejson

def main(args):
    #Load file and store hashes in index file
    prefs = boxchannel.initUserPreferences()
    if not os.path.exists(prefs['indexDirectory']):
        os.makedirs(prefs['indexDirectory'])

    indexFileName = os.path.join(prefs['indexDirectory'], "%s.index" % prefs['id'])
    indexFile = file(indexFileName, 'w')
    for fileName in args:
        print "Indexing", fileName
        newFile = file(fileName, 'r')
        lineElements = [os.path.abspath(fileName)]
        for blockHash in boxchannel.hashesFor(newFile):
            lineElements.append(blockHash)
        line = simplejson.dumps(lineElements)
        assert "\n" not in line
        indexFile.write(line)
        indexFile.write("\n")
    indexFile.close()

if __name__ == "__main__":
    main()
