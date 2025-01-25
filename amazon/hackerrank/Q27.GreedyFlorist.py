#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    if k >= len(c):
        return sum(c)

    c.sort(reverse=True)
    price = 0

    for i in range(k):
        price += c[i]

    times = 2
    reset = k
    for i in range(k, len(c)):
        price += c[i] * times
        reset -= 1
        if reset == 0:
            times += 1
            reset = k

    return price

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
