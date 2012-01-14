#!/usr/bin/python
import boxchannel
import sys
import glob
import os
import datetime

def main(args):

    #Load or generate user preferences
    prefs = boxchannel.initUserPreferences()
    
    #Load all index files, see if we can find the mentioned file
    indexFileDirectory = prefs['indexDirectory']
    requestDirectory = prefs['requestDirectory']
    stageDirectory = prefs['stageDirectory']

    if not os.path.exists(prefs['requestDirectory']):
        os.makedirs(prefs['requestDirectory'])

    if len(args) < 1:
        print "No file requested, listing all files indexed"
        for pathAndHashes in boxchannel.indexedFiles(indexFileDirectory):
            fullPath = pathAndHashes.pop(0)
            print os.path.basename(fullPath)
        return
    requestedFile = args.pop()
    
    print "Looking for:", requestedFile  
    requestMade = False  
    for pathAndHashes in boxchannel.indexedFiles(indexFileDirectory):
        fullPath = pathAndHashes.pop(0)
        hashes = pathAndHashes
        if os.path.basename(fullPath) == requestedFile:
            #Found the file
            requestMade = True
            print "Requesting:", fullPath
            requestStageDirectory = os.path.join(stageDirectory, requestedFile)
            
            if not os.path.exists(requestStageDirectory):
                os.mkdir(requestStageDirectory)
            
            for (blockIndex, h) in enumerate(hashes):
                h = h.strip() #Remove newline if it is on the line
                stageName = os.path.join(requestStageDirectory, "%s.%s" %(h, blockIndex))
                requestName = os.path.join(requestDirectory, h)
                print "Creating file:", requestName
                file(requestName, 'w').close()
                file(stageName, 'w').close()
    if not requestMade:
        print "Could not find requested file"
        return 1
    return 0
if __name__ == "__main__":
    main()
