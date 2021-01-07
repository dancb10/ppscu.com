from collections import deque

dq = deque(range(10), maxlen=10)
dq.rotate(3)
dq.rotate(-4)
dq.appendleft(-1)
dq.appendleft(-1)
dq.extend([11, 22, 33])
mber
