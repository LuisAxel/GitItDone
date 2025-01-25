#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def sherlockAndAnagrams(s):
    substrings = {}
    count = 0

    for left in range(0, len(s)):
        for right in range(left + 1, len(s) + 1):
            current = s[left:right]
            current = "".join(sorted(current))
            substrings[current] = substrings.get(current, 0) + 1

    for val in substrings.values():
        if val == 1:
            continue
        count += val * (val - 1) // 2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
