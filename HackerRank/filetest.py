
with open('input.txt') as f:
    offset = f.tell()
    print(offset)
    line = f.readline()
    print(line)
    offset = f.tell()
    print(offset)
