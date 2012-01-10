#!/usr/bin/python
import boxchannel
import sys
import glob
import os
import datetime
#Stage directory is:
#   filename/block.idx
def main():
    #Move all of our requests from the response directory into the stage directory
    prefs = boxchannel.loadUserPreferences()
    stageDirectory = prefs['stageDirectory']
    responseDirectory = prefs['responseDirectory']
    
    #For each of the responses, move it if we have an empty staged block for it
    for responseName in glob.glob(os.path.join(responseDirectory, "*")):
        blockHash = os.path.basename(r)
        stageFile = os.path.join(stageDirectory, blockHash)
        stageFiles = glob.glob(os.path.join(stageDirectory, "*", blockHash + ".*")) #Find any staged file needing the block
        if len(stageFiles) > 0:
            removeResponse = False
            block = file(responseName, 'r').read(boxchannel.blockSize)
            for stageFile in stageFiles:
                if os.path.getsize(stageFile) == 0:
                    print "Realing in", blockHash
                    removeResponse = True
                    file(stageFile, 'w').write(block)
            if removeResponse:
                print "Realing in", blockHash
                os.unlink(stageFile)
        
    #See if we can patch up a file from the staged blocks, patch it up and clean the directory
    for stageFileDirectory in glob.glob(os.path.join(stageDirectory, "*")):
        complete = True
        for blockFile in glob.glob(os.path.join(stageFileDirectory, "*")):
            if os.path.getsize(blockFile) == 0:
                complete = False
                break
        if complete:
            #Bundle into Downloads directory
            print "Complete download:", os.path.basename(stageFileDirectory)
            print "TODO: order chunks, write to Downloads directory"
    
if __name__ == "__main__":
    main()

