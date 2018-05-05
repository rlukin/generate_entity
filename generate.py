import numpy as np
import entities

import multiprocessing
import sys


count = 32768
buffer_size = 8192


def worker():
    np.random.seed(int(multiprocessing.current_process().pid))
    for i in range(cycles):
        data = entities.generate_entities(count)

        data_csv = ''
        buffer_counter = 0

        for row in data[0]:
            data_csv += '"' + '","'.join(row) + '"\n'   # :-)
            buffer_counter += 1
            if buffer_counter >= buffer_size:
                print data_csv
                buffer_counter = 0
                data_csv = ''

        if buffer_counter < buffer_size:
            print data_csv

    return


if __name__ == '__main__':
    # simple argparse based on assumption that one cycle generates 67 mbs and
    # one record ~320 bytes
    argv = int(sys.argv[1])
    if argv > 67:
        workers_amount = multiprocessing.cpu_count()
        cycles = int(1024*1024*argv/float(320*count)/workers_amount)
    else:
        cycles = workers_amount = 1
        count = int(1024*1024*argv/float(320)) + 1
        print count

    jobs = []
    for i in range(workers_amount):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
