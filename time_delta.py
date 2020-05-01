#!/bin/python3

import os
from datetime import datetime

def time_delta(t1, t2):
    # Parse date strings into datetime objects
    dt_object_t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    dt_object_t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

    # Get absolute time delta and return in seconds
    delta = abs(dt_object_t1 - dt_object_t2)
    return str(int(delta.total_seconds()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
