#!/usr/bin/python
import mmh3
import glob
import base64
import sys
import logging

blockSize = 1024*1024


class LocalBlock:
    def __init__(self, filename, index):
        self._index = index
        self._filename = filename


def blockHash(block):
    hashBytes = mmh3.hash_bytes(block)
    return base64.urlsafe_b64encode(hashBytes)
    

def hashesFor(f):
    data = f.read(blockSize)
    yield blockHash(data)

def publishBlock(blockInfo):
    logging.log("publishing: %s", blockInfo)
    


def main():
    knownBlocks = {}
    #Load database
    for fileName in sys.argv[1:]:
        logging.info("Loading local block info from: %s", fileName)
        of = file(fileName, 'r')
        idx = 0
        for blockHash in hashesFor(of):
            knownBlocks[blockHash] = LocalBlock(fileName, idx)
            idx += 1
    logging.info("Loaded %i blocks", len(knownBlocks))
    
    #Respond to requests
    for requestFile in glob.glob("request/*"):
        if requestFile in knownBlocks:
            publishBlock(knownBocks[requestFile])
    
    #cleanRequests()
    #cleanResponses()
    
    


if __name__ == "__main__":
    main()
