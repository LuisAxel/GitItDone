#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max_hourglass_sum = float('-inf')

    for y in range(4):
        for x in range(4):
            curr = 0
            curr += arr[y][x] + arr[y][x + 1] + arr[y][x + 2]
            curr += arr[y + 1][x + 1]
            curr += arr[y + 2][x] + arr[y + 2][x + 1] + arr[y + 2][x + 2]
            max_hourglass_sum = max(max_hourglass_sum, curr)

    return max_hourglass_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
