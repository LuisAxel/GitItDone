#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    left, right = {}, {}

    for k in arr:
        right[k] = right.get(k, 0) + 1

    triplets = 0
    for j in arr:
        right[j] -= 1

        if j % r == 0:
            i = j // r
            k = j * r
            triplets += left.get(i, 0) * right.get(k, 0)

        left[j] = left.get(j, 0) + 1

    return triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
