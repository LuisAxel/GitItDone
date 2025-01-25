#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inversions = merge_sort(arr[:mid])
    right, right_inversions = merge_sort(arr[mid:])

    merged, merge_inversions = merge(left, right)

    return merged, merge_inversions + left_inversions + right_inversions

def merge(left, right):
    merged = []
    l, r = 0, 0
    inversions = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            inversions += len(left) - l
            r += 1
    merged.extend(left[l:])
    merged.extend(right[r:])
    return merged, inversions

def countInversions(arr):
    return merge_sort(arr)[1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
