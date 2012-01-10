#!/usr/bin/python
import boxchannel
import sys
import glob
import os
import datetime

def main():

    requestedFile = sys.argv[1]
    print "Looking for:", requestedFile    
    #Load or generate user preferences
    prefs = boxchannel.initUserPreferences()
    
    #Load all index files, see if we can find the mentioned file
    indexFileDirectory = prefs['indexDirectory']
    requestDirectory = prefs['requestDirectory']
    stageDirectory = prefs['stageDirectory']

    for indexFileName in glob.glob(os.path.join(indexFileDirectory, "*.index")):
        indexFile = file(indexFileName, 'r')
        for line in indexFile.xreadlines():
            (fullPath, hashes) = line.split(" || ", 1)
            if os.path.basename(fullPath) == requestedFile:
                #Found the file
                print "Requesting:", fullPath
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H")
                
                os.mkdir(os.path.join(stageDirectory, requestedFile))
                for (blockIndex, h) in enumerate(hashes.split(" ")):
                    h = h.strip() #Remove newline if it is on the line
                    stageName = os.path.join(stageDirectory, requestedFile, "%s.%s" %(h, blockIndex))
                    requestName = os.path.join(requestDirectory, "%s.%s" %(h, timestamp))
                    print "Creating file:", requestName
                    file(requestName, 'w').close()
                    file(stageName, 'w').close()
            #else:
            #    print "Not requesting", fullPath

if __name__ == "__main__":
    main()
