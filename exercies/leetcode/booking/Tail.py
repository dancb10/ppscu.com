# implement tail -f
import time
import os


def tailf(tail_file):
    with open(tail_file) as file_:
        # Go to the end of file
        file_.seek(0, 2)
        while True:
            curr_position = file_.tell()
            line = file_.readline()
            if not line:
                file_.seek(curr_position)
                time.sleep(1)
            else:
                print(line)
