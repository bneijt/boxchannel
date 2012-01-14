#!/usr/bin/python
import boxchannel
import sys
import glob
import os
import datetime

def main():

    #Load or generate user preferences
    prefs = boxchannel.initUserPreferences()
    
    #Load all index files, see if we can find the mentioned file
    indexFileDirectory = prefs['indexDirectory']
    requestDirectory = prefs['requestDirectory']
    stageDirectory = prefs['stageDirectory']

    if not os.path.exists(prefs['requestDirectory']):
        os.makedirs(prefs['requestDirectory'])

    if len(sys.argv) < 2:
        print "No file requested, listing all files indexed"
        for (fullPath, hashes) in boxchannel.indexedFiles(indexFileDirectory):
            print os.path.basename(fullPath)
        return
    requestedFile = sys.argv[1]
    
    print "Looking for:", requestedFile    
    for (fullPath, hashes) in boxchannel.indexedFiles(indexFileDirectory):
        if os.path.basename(fullPath) == requestedFile:
            #Found the file
            print "Requesting:", fullPath
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H")
            requestStageDirectory = os.path.join(stageDirectory, requestedFile)
            if not os.path.exists(requestStageDirectory):
                os.mkdir(requestStageDirectory)
            
            for (blockIndex, h) in enumerate(hashes.split(" ")):
                h = h.strip() #Remove newline if it is on the line
                stageName = os.path.join(requestStageDirectory, "%s.%s" %(h, blockIndex))
                requestName = os.path.join(requestDirectory, "%s.%s" %(h, timestamp))
                print "Creating file:", requestName
                file(requestName, 'w').close()
                file(stageName, 'w').close()

if __name__ == "__main__":
    main()
