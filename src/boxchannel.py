#!/usr/bin/python
import mmh3
import glob
import binascii
import sys
import logging
import hashlib

blockSize = 1024*1024*10


class LocalBlock:
    def __init__(self, filename, index):
        self._index = index
        self._filename = filename


def blockHash(block):
    hashBytes = mmh3.hash_bytes(block)
    return binascii.hexlify(hashBytes)


def hashesFor(f):
    data = f.read(blockSize)
    yield blockHash(data)

def publishBlock(blockInfo):
    logging.log("publishing: %s", blockInfo)
    


def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    knownBlocks = {}
    #Load database
    for fileName in sys.argv[1:]:
        logging.info("Loading local block info from: %s", fileName)
        of = file(fileName, 'r')
        idx = 0
        for blockHash in hashesFor(of):
            knownBlocks[blockHash] = LocalBlock(fileName, idx)
            logging.info("Loaded %s", blockHash)
            idx += 1
    logging.info("Loaded %i blocks", len(knownBlocks))
    
    
    #Respond to requests
    for requestFile in glob.glob("request/*"):
        logging.info("Found request: %s", requestFile)
        requestHash = requestFile.split(".", 1)[0]
        if requestHash in knownBlocks:
            publishBlock(knownBlocks[requestHash])
    logging.info("EXIT")
    #cleanRequests()
    #cleanResponses()
    
    


if __name__ == "__main__":
    main()
