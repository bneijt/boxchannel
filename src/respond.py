#!/usr/bin/python
import boxchannel
import sys
import glob
import os
import datetime

def main():
    prefs = boxchannel.loadUserPreferences()
    requestDirectory = prefs['requestDirectory']
    indexFileDirectory = prefs['indexDirectory']
    responseDirectory = prefs['responseDirectory']

    if not os.path.exists(prefs['responseDirectory']):
        os.makedirs(prefs['responseDirectory'])
    
    indexFileName = os.path.join(indexFileDirectory, "%s.index" % prefs['id'])
    indexFile = file(indexFileName, 'r')
    
    #Load all requests in memory
    requests = {}
    for request in glob.glob(os.path.join(requestDirectory, "*")):
        (requestedHash, timestamp) = os.path.basename(request).split(".")
        requests[requestedHash] = timestamp
    
    #See if we have that block in our index
    for line in indexFile.xreadlines():
        (fullPath, hashes) = line.split(" || ", 1)
        for (blockIdx, h) in enumerate(hashes.split(" ")):
            h = h.strip() #Remove newline if it is on the line
            if h in requests:
                print "Responding to", h
                #Respond with our file hash
                responseFile = os.path.join(responseDirectory, h)
                localFile = file(fullPath, 'r')
                IOS_BEG = 0
                localFile.seek(blockIdx * boxchannel.blockSize, IOS_BEG)
                block = localFile.read(boxchannel.blockSize)
                localFile.close()
                rf = file(responseFile, 'w')
                rf.write(block)
                rf.close()
                for requestName in glob.glob(os.path.join(requestDirectory, h + ".*")):
                    print "Removing", requestName
                    os.unlink(requestName)
    
    
if __name__ == "__main__":
    main()
