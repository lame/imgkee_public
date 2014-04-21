# This is the salting processing backend for imgKee.
#   The functions and objects in this file are used to do simple salting of
#   image pixel data.

# Authors: Preston Hamlin

# Currently only supports BMP images.
# Currently does not do analysis of pixels to make changes more discrete
# Code may be broken into helper functions or more complicated salting

# Will be broken into a callable function and a usable object. THe object will
#    be used in the case where it is desirable to retain state for bulk hashing.
#    The function will be used to salt a single image in-place.


import os, sys, binascii, random
from image import  *


# callable Uniq function creates temp UniqClass object for immediate use
def Uniq(file, mode=0, param0=0, param1=0):    
    path = os.getcwd() + '/' + file
    q = UniqClass(path, mode, 20)
    q.Salt()
    
    
class UniqClass:
    def __init__(self, path, mode=1, num_ops=1, brush_size=1, strength=0.5):       
        self.path       = path
        self.mode       = mode
        self.num_ops    = num_ops
        self.brush_size = brush_size
        self.strength   = strength
        
        self.imgdata    = GetImageMode(path)
        
        self.functions = (self.SaltByBytes,
                          self.SaltByPixels,
                          self.SimpleBlur,
                          self.BetterBlur,
                          self.LowKeySalt)
        
    def Salt(self):
        if not os.path.exists(self.path):
            sys.stderr.write('\nERROR: Cannot locate file for salting\n')
            return 0
        if not self.imgdata:
            sys.stderr.write('\nERROR: Cannot salt unsupported file type\n')
            return 0
        self.functions[self.mode]()
        return 1
        
        
    def SaltByBytes(self):                      # salt by shifting byte
        if isinstance(self.imgdata, BMPImage):
            for i in range(self.num_ops):
                loc = self.imgdata.h_pixel_loc
                end = loc + self.imgdata.d_size
                self.imgdata.writebuffer[random.randint(loc, end)] = \
                    struct.pack('B', random.randint(0, 255))
            self.imgdata.Write()
        
        # PNG only has one salt function
        elif isinstance(self.imgdata, PNGImage):
            self.imgdata.Salt(self.num_ops)
                
            
            
        else:
            print("SaltByBytes not yet finished")
    
    
    def SaltByPixels(self):                     # salt by shifting bytes
        print("SaltByPixels not yet finished")
    
    
    def SimpleBlur(self):                       # salt by simple blur
        if isinstance(self.imgdata, BMPImage):
            
            for i in range(self.num_ops):
                loc = self.imgdata.h_pixel_loc
                end = loc + self.imgdata.d_size
                
                x = random.randint(0, self.imgdata.d_width)
                y = random.randint(0, self.imgdata.d_height)
                
                R = G = B = 0

                    
                self.imgdata.writebuffer[random.randint(loc, end)] = \
                    struct.pack('B', random.randint(0, 255))
            self.imgdata.Write()
        
        # PNG only has one salt function
        elif isinstance(self.imgdata, PNGImage):
            self.imgdata.Salt(self.num_ops)

    def BetterBlur(self):                       # salt by advanced blur
        print("BetterBlur not yet finished")
        
        
    def LowKeySalt(self):                       # advanced low-key salt
        print("LowKeySalt not yet finished")


   





def GetPixel(path, w, h, x, y, bpp):
    ifile = open(path, 'rb')
    
    




        
if __name__ == "__main__":
    # you can call the function Uniq on a file and move on
    Uniq("hello.txt", 4)
        