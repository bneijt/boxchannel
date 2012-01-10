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
    
    for indexFileName in glob.glob(os.path.join(indexFileDirectory, "*.index")):
        indexFile = file(indexFileName, 'r')
        for line in indexFile.xreadlines():
            (fullPath, hashes) = line.split(" || ", 1)
            if os.path.basename(fullPath) == requestedFile:
                #Found the file
                print "Requesting:", fullPath
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H")
                for h in hashes.split(" "):
                    h = h.strip() #Remove newline if it is on the line
                    requestName = os.path.join(requestDirectory, "%s.%s" %(h, timestamp))
                    print "Creating file:", requestName
                    file(requestName, 'w').close()
            #else:
            #    print "Not requesting", fullPath

if __name__ == "__main__":
    main()
