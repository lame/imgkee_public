# Test script for the Hashify function.



import os, sys

sys.path.append("../src/processing/python_src")
from hashify import *




if __name__ == '__main__':
    print("\nCurrent directory:")
    print(os.getcwd())
    print("\nCurrent directory contents:")
    print(os.listdir(os.getcwd()))
    
    print("\n\n\n====== Several hashes using differing algorihms: ======")
    #MD5
    print("Hash of small.bmp - mode=0 (MD5)")
    print(Hashify("small.bmp", 0))
    #SHA1
    print("\nHash of small.bmp - mode=1 (sha1)")
    print(Hashify("small.bmp", 1))
    #sha224
    print("\nHash of small.bmp - mode=2 (sha224)")
    print(Hashify("small.bmp", 2))
    #sha256
    print("\nHash of small.bmp - mode=3 (sha256)")
    print(Hashify("small.bmp", 3))
    #sha384
    print("\nHash of small.bmp - mode=4 (sha384)")
    print(Hashify("small.bmp", 4))
    #sha512
    print("\nHash of small.bmp - mode=5 (sha512) - DEFAULT")
    print(Hashify("small.bmp", 5))
    
    
    
    print("\n\n\n====== Testing relative file paths: ======")

    print("local directory   - small.bmp")
    print(Hashify("small.bmp", 0))

    print("\nsub-directory     - subdir/text.txt")
    print(Hashify("subdir/text.txt", 0))
    
    print("\nfunky path        - ../samples/.././hello.txt")
    print(Hashify("../samples/.././hello.txt", 0))
    
    
    
    
    
    
    
    
    
    
    
    
    
    