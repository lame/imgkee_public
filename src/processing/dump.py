import binascii
ff = open("cat.png", "rb")
data = ff.read()
ff.close()

txt = binascii.hexlify(data)

fw = open("cat.txt", "wb")
fw.write(txt)
fw.close()