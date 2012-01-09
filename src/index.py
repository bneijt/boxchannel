#!/usr/bin/python
import boxchannel
import os
import sys

def main():
    #Load file and store hashes in index file
    prefs = boxchannel.initUserPreferences()
    indexFileName = os.path.join(prefs['indexDirectory'], "%s.index" % prefs['id'])
    indexFile = file(indexFileName, 'w')
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
