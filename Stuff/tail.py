import sys
# lines = 10
#
# with open('file.txt', 'r') as f:
#     f.seek(0,2)
#     while True:
#         current_position = f.tell()
#         line = f.readline()
#         print(line)
def print_tail_lines2(n: int):
    with open('file.txt', 'r') as f:
        lines = f.readlines()
        for i in range(1, n):
            print(lines[-i].rsplit())

def print_tail_lines(n: int):
    with open('file.txt', 'rb') as f:
        f.seek(0, 2)
        while f.read() == '\n':


        # f.read(1).decode('utf-8')
        # current_position=f.tell()
        line = f.readline()
        print(line)
    # with open('file.txt', 'r') as f:
    #     for index in range(n):
    #
    #         line = f.readline()
    #         print(line)

def print_head_lines():
    pass

def follow_lines_infile():
    pass

print_tail_lines2(10)


