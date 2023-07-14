
truth = 200
b1 = '{0:32b}'.format(truth)
bi = bin(truth).replace("0b","")
b2 = bi.zfill(32)
d1 = int(b1, 2)
d2 = int(b2, 2)



print()
print('Truth            : ', truth)
print('Binary method 1  : ', b1)
print('Binary method 2  : ', b2)
print('Decimal method 1 : ', d1)
print('Decimal method 2 : ', d2)
print()
