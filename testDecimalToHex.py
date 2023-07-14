
d = 200

hex(d)
h = hex(200).replace("0x", "")
h.zfill(4)
print('Hex method 1 :', h)

h2 = '{0:08x}'.format(d).replace(" ", "0")
print('Hex method 2:', h2)
