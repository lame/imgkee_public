import hashlib

ff = open("cat.txt", "rb")
txt = ff.read()

m = hashlib.sha512()
m.update(txt)
key = m.digest()

print(key)