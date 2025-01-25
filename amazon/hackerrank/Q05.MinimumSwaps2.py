#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    idx, n = 0, len(arr)
    while idx < n:
        val = arr[idx]
        if idx == val - 1:
            idx += 1
            continue
        count += 1
        arr[idx], arr[val - 1] = arr[val - 1], arr[idx]

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
