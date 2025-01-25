#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    i = 0
    while i < n:
        same_char_count = 1
        j = i + 1
        while j < n and s[i] == s[j]:
            j += 1
            same_char_count += 1

        count += same_char_count

        odd_one = j
        j += 1
        while j < n and s[i] == s[j]:
            if j - odd_one == odd_one - i:
                count += 1
                break
            j += 1

        i += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
