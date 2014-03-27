import binascii
import hashlib


def dump():
	ff = open("cat.png", "rb")
	data = ff.read()
	ff.close()

	txt = binascii.hexlify(data)

	fw = open("cat.txt", "wb")
	fw.write(txt)
	fw.close()

def hash():
	ff = open("cat.txt", "rb")
	txt = ff.read()

	m = hashlib.sha512()
	m.update(txt)
	key = m.digest()

	print(key)