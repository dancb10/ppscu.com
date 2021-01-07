l=list(range(10))
l[2:5]=[20,30,40]
del(l[3:6])
l.sort()
sorted(l)
l[2:5]=[100]

board = [['_'] * 3 for i in range(3)]
board[2][3]='X'

board=[['_'] * 3]
board=[['_'] * 3] * 3
