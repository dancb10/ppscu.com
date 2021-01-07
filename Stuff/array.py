from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
floats2=floats.__copy__()

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()

