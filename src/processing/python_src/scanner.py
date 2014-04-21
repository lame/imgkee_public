# This is the scanning processing backend for imgKee.
#   The functions and objects in this file are used to do simple scanning of
#   image pixel data to find potential hazards such as executables.

# Authors: Preston Hamlin

# scans file, returns string containing warnings, or 0 if error
# loads entire file into memory, in chunks
# For better results, look at pixel regions to determine if there are large 
#    blocks of identical data, meaning good chance of it being just an image.
#    Also, check to see if headers are corrupted, gaps filled, etc...


# Currently, a risk of 7 or more is high, and below 4 is low.
#    Around 20 is very high.
#    Binaries that use DLLs have a low score, making them seem to be images.
SCANSIZE = 32

import os, sys
from hashify import *
from image import GetImageMode

def Scan(filename):
    path = os.getcwd() + '/' + filename
    if not os.path.exists(path):
        sys.stderr.write('\nERROR: Cannot locate file for scanning\n')
        return 0
    
    ifile = open(path, 'rb')
    
    risk = 0
    buffer      = ifile.read(SCANSIZE)
    last        = 0
    


    
    while (buffer):
        val = buffer[0]
        
        # short jumps
#        if (val >= 0x70) and (val <= 0x7f):
#            risk += 1
        # unconditional and conditional jump
#        if (val >= 0xe9) and (val <= 0xeb):
#            risk += 1
#        if (val == 0xff):    # white pixel...
#            risk += 20
        
        # common data ops
        if (val == 0x8b) or (val == 0x89):
            risk += 20
        if (val == 0xc0) or (val == 0xc1):
            risk += 10
        if (val == 0x01) or (val == 0x03):
            risk += 10
        
        if (val == last):   # repeated commands
            risk += 1
        
        last    = val
        buffer  = ifile.read(SCANSIZE)
    
    risk /= (os.path.getsize(path)/256)
    
    
    if not GetImageMode(path):
        risk += 10
    
    
    print("\nRisk: " + str(risk))
    return risk



