#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = n
    for i in range(n):
        diff_idx = -1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if diff_idx == -1:
                    count += 1
                elif j - diff_idx == diff_idx - i:
                    count += 1
                    break
            else:
                if diff_idx != -1:
                    break
                diff_idx = j

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
