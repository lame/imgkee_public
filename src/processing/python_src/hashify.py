# This is the hashing processing backend for imgKee.
#   The functions and objects in this file are used to do simple hashing of
#   image pixel data.
#
# NOTE: These functions work with local files and relative filepaths. The paths
#   are relative to wherever Python was executd from, and NOT where this source
#   file is located. If you import this as a module, then you need to make file
#   names and working directories (where you store image files) relative to 
#   wherever Python is first called from.

# Authors: Preston Hamlin

import hashlib, os, sys

CHUNK_SIZE          = 64
AvailableHashers    = ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')
cwd                 = os.getcwd()

# returns a hex hash string, or 0 if file cannot be found
def Hashify(filename, mode=5, quiet=0):
    h = Hasher(mode)
    if not h.LoadFile(GetTruePath(filename)):
        if not quiet:
            sys.stderr.write('\nERROR: Cannot locate file "' + filename + '"\n')
        return 0
    else:
        return h.Digest()

def GetTruePath(local_path):
    return (cwd + '/' + local_path)




# Prevents entire file from being loaded into memory at once.
#
# HOWEVER, the actual Python implementation simply appends data to a buffer
#   and then recomputes the hash. The entire object WILL be in memory as part
#   of the hashlib object. This simply prevents the entire file from being
#   LOADED at once, which would cause an amount of memory twice the size to
#   be used: 1x for the buffer below, 1x for the python hash object buffer
#
# To truly not have the entire file residing in memory at once, one must hash
#   the chunks, store the hashes (much smaller in size) and then combine these
#   multiple hashes together in some manner. Perhaps hash them?
class Hasher:
    def __init__(self, mode=5):
        self.digest = ""
        self.mode = mode
                

    def LoadFile(self, filepath):
        if not os.path.exists(filepath):        # bad file path
            return 0
        
        alg = hashlib.new(AvailableHashers[self.mode])
        ifile = open(filepath, "rb")
        
        buffer = ifile.read(CHUNK_SIZE)
        while(buffer):
            alg.update(buffer)
            buffer = ifile.read(CHUNK_SIZE)

        self.digest =   alg.hexdigest()
        return 1
                                         
    def Digest(self):
        return self.digest
                            
                            

    