from array import array
numbers = array.array('h', [-2, -1, 0, 1, 2])

memv = memoryview(numbers)

memv_oct = memv.cast('B')
memv_oct.tolist()
memv_oct[5] = 4
