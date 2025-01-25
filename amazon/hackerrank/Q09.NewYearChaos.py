#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes = 0

    for idx, val in enumerate(q):
        if val - idx > 3:
            print("Too chaotic")
            return

        for bribe_giver_idx in range(max(0, val - 2), idx):
            if q[bribe_giver_idx] > val:
                bribes += 1
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
