import multiprocessing as mp
import os

def map_lines(offset):
    with open("input.txt") as f:
        f.seek(offset)
        current_line = f.readline()

        print(current_line)



def main():
    pool = mp.Pool(processes=os.cpu_count())
    jobs = []
    with open("input.txt") as f:
        offset = f.tell()
        for line in f:
            jobs.append(pool.apply_async(map_lines, (offset,)))
            offset = f.tell()

    pool.close()

main()
