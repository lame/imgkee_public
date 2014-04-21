# contains classes for reading/writing of data to image files

import os, sys, binascii, struct

# parent class of all image classes
class Image:
    def __init__(self, path):
        self.path = path
        self.writebuffer = {}
    
    def Write(self):
        ofile = open(self.path, 'r+b')
        
        for key in self.writebuffer.keys():
#            print(str(key) + " -> " + str(self.writebuffer[key]))
            ofile.seek(key)
            ofile.write(self.writebuffer[key])
#            input()

        ofile.close()
            
class BMPImage(Image):
    def __init__(self, path):
        super().__init__(path)
        ifile = open(self.path, 'rb')
        
        self.bmp_header     = bytearray( ifile.read(14) )
        dib_size            = struct.unpack('<I', bytearray(ifile.read(4)))[0]
      
        # only supporting most common header format
        if dib_size == 40:
            self.dib_format = "BITMAPINFOHEADER"
        else:
            sys.stderr.write('\nERROR: Unsupported BMP format\n')
            return 0
            
        ifile.seek(14)
        self.dib_header     = bytearray( ifile.read(dib_size) )
        
        # unpack file header
        self.h_ID, self.h_size, self.h_u1, self.h_u2, self.h_pixel_loc  \
            = struct.unpack('<2sIHHI', self.bmp_header)
        
        # unpack DIB header
        self.d_hsize,   self.d_width,   self.d_height,  self.d_planes,  \
        self.d_BPP,     self.d_comp,    self.d_size,    self.d_horiz,   \
        self.d_vert,    self.d_colors,  self.d_icolors                  \
            = struct.unpack('<IiiHHIIiiII', self.dib_header)
        
        
        #self.pixel_padding = \
        #    ( (self.d_width * self.d_height)*self.d_BPP / 8)
        
        
#        self.Print()
        ifile.close()
        
        
# print function prints member data for debugging
    def Print(self):
        print('\nSubtype:         {}'\
            '\nFile Size:       {}'\
            '\nU1:              {}'\
            '\nU2:              {}'\
            '\nPixels start:    {}'\
            ''.format( self.h_ID.decode('utf-8'),   self.h_size,    self.h_u1, \
                       self.h_u2,   self.h_pixel_loc) ) 
        print('\nDIP Header Size:         {}'\
            '\nWidth:                   {}'\
            '\nHeight:                  {}'\
            '\nPlanes:                  {}'\
            '\nBPP:                     {}'\
            '\nCompression Mode:        {}'\
            '\nImage Size:              {}'\
            '\nHorizontal Resolution:   {}'\
            '\nVertical Resolution:     {}'\
            '\nColor Palette Size:      {}'\
            '\nImportant Colors:        {}'\
            '\n'.format( \
                 self.d_hsize,  self.d_width,   self.d_height,  self.d_planes,\
                 self.d_BPP,    self.d_comp,    self.d_size,    self.d_horiz, \
                 self.d_vert,   self.d_colors,  self.d_icolors) )
        
class PNGImage(Image):
    def __init__(self, path):
        super().__init__(path)
        ifile = open(self.path, 'rb')
        
        
        ifile.close()
        
    
class JPGImage(Image):
    def __init__(self, path):
        super().__init__(path)
        ifile = open(self.path, 'rb')

        
        ifile.close()

    
class GIFImage(Image):  
    def __init__(self, path):
        super().__init__(path)
        ifile = open(self.path, 'rb')
        
        
        ifile.close()
        



      
# returns mode (filetype), or 0 if not supported
def GetImageMode(path):
    if not os.path.exists(path):
        sys.stderr.write('\nERROR: Cannot locate file:\n' + path + '\n')
        return 0
    
    ifile = open(path, 'rb')
    tag = ifile.read(8)
    ifile.close()
       
    if   binascii.hexlify(tag)[0:4]     == b'424d':
        return BMPImage(path)           # Windows Bitmap
    elif binascii.hexlify(tag)[0:16]    == b'89504e470d0a1a0a':
        return PNGImage(path)           # PNG image
    elif binascii.hexlify(tag)[0:6]     == b'ffd8ff':
        return JPGImage(path)           # JPG image
    elif binascii.hexlify(tag)[0:12]    == b'474946383961':
        return GIFImage(path)           # GIF 89a
    elif binascii.hexlify(tag)[0:12]    == b'474946383761':
        sys.stderr.write('\nWARNING: old GIF format detected')
        return GIFImage(path)           # GIF 87a
    else:
        return 0                        # invalid or unsupported file type
        
        
