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
    downloadDirectory = prefs['downloadDirectory']
    stageDirectory = prefs['stageDirectory']
    responseDirectory = prefs['responseDirectory']

    if not os.path.exists(prefs['stageDirectory']):
        os.makedirs(prefs['stageDirectory'])
    
    #For each of the responses, move it if we have an empty staged block for it
    for responseName in glob.glob(os.path.join(responseDirectory, "*")):
        blockHash = os.path.basename(responseName)
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
                print "Removing", responseName
                os.unlink(responseName)
    
    #See if we can patch up a file from the staged blocks, patch it up and clean the directory
    for stageFileDirectory in glob.glob(os.path.join(stageDirectory, "*")):
        complete = True
        blockFiles = glob.glob(os.path.join(stageFileDirectory, "*"))
        if len(blockFiles) > 0:
            for blockFile in blockFiles:
                if os.path.getsize(blockFile) == 0:
                    complete = False
                    break
        else:
            complete = False
        if complete:
            #Bundle into Downloads directory
            downloadName = os.path.basename(stageFileDirectory)
            print "Complete download:", downloadName
            blockFilesSorted = [None] * len(blockFiles)
            print "Size: %i times %i bytes" % (len(blockFiles), boxchannel.blockSize)
            for bfn in blockFiles:
                (h, idx) = os.path.basename(bfn).split(".", 1)
                blockFilesSorted[int(idx)] = bfn
            
            if None in blockFilesSorted:
                raise Exception("Could not find one of the file blocks")
            outputFileName = os.path.join(downloadDirectory, downloadName)
            outputFile = file(outputFileName, 'w')
            for blockFileName in blockFilesSorted:
                print "Writing:", blockFileName
                with open(blockFileName) as blockFile:
                    block = blockFile.read(boxchannel.blockSize)
                    outputFile.write(block)
                os.unlink(blockFileName)
            print "Written:", outputFileName
    
if __name__ == "__main__":
    main()

