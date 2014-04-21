# Test script for the Hashify function.



import os, sys, shutil

sys.path.append("../src/processing/python_src")
from uniq import *
from hashify import *


if __name__ == '__main__':
    print("\nCurrent directory:")
    print(os.getcwd())
    print("\nCurrent directory contents:")
    print(os.listdir(os.getcwd()))
    
    print("\n\n\n====== Demonstrating class generation from files: ======")
    print("Windows Bitmap (BMP)                      -    small.bmp")
    print(GetImageMode("small.bmp"))
    
    print("\nPortable Network Graphics (PNG)           -    other.png")
    print(GetImageMode("other.png"))
    
    print("\nJoint Photographic Experts Group (JPG)    -    another.jpg")
    print(GetImageMode("another.jpg"))
    
    print("\nGraphics Intechange Format (GIF)          -    gif.gif")
    print(GetImageMode("gif.gif"))
    
    print("\nNot an image                              -    text.txt")
    print(GetImageMode("subdir/text.txt"))
    
    
    # will overwrite an existing file named small-copy.bmp
    print("\n\n\n====== Hashing salted copy of image: ======")
    print("Hash of small.bmp - (sha256)")
    print(Hashify("small.bmp", 3))
    
    # Salt by bytes
    print("\nHash of small-copy.bmp - salt by bytes")
    shutil.copyfile("small.bmp", "small-copy.bmp")      # copy file
    Uniq("small-copy.bmp", 0)                        # salt the copy
    print(Hashify("small-copy.bmp", 3))              # print hash of copy
   
    input("\nPress return key to move on to next salting demo...")
#    
#    print("\nHash of small-copy.bmp - salt by pixels")
#    shutil.copyfile("small.bmp", "small-copy.bmp")      # copy file
#    Uniq("small-copy.bmp", 1)                        # salt the copy
#    print(Hashify("small-copy.bmp", 3))              # print hash of copy
#    
#    input("\nPress return key to move on to next salting demo...")
#    
#    print("\nHash of small-copy.bmp - simple blur")
#    shutil.copyfile("small.bmp", "small-copy.bmp")      # copy file
#    Uniq("small-copy.bmp", 2)                        # salt the copy
#    print(Hashify("small-copy.bmp", 3))              # print hash of copy
#    
#    input("\nPress return key to move on to next salting demo...")
#    
#    print("\nHash of small-copy.bmp - better blur")
#    shutil.copyfile("small.bmp", "small-copy.bmp")      # copy file
#    Uniq("small-copy.bmp", 3)                        # salt the copy
#    print(Hashify("small-copy.bmp", 3))              # print hash of copy
#    
#    input("\nPress return key to move on to next salting demo...")
#    
#    print("\nHash of small-copy.bmp - low-key salt")
#    shutil.copyfile("small.bmp", "small-copy.bmp")      # copy file
#    Uniq("small-copy.bmp", 4)                        # salt the copy
#    print(Hashify("small-copy.bmp", 3))              # print hash of copy
    
    
#    input("\nPress return key to move on to next salting demo...")
    
    
    
    
    print("\n\n\n====== Hashing salted copy of image: ======")
    print("Hash of other.png - (sha256)")
    print(Hashify("other.png", 3))
    
    #salt by bytes, PNG
    print("\nHash of other-copy.png - salt by bytes")
    shutil.copyfile("other.png", "other-copy.png")      # copy file
    Uniq("other-copy.png", 0)                        # salt the copy
    print(Hashify("other-copy.png", 3))              # print hash of copy
    
    
    
    
