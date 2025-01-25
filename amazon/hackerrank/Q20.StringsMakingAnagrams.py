#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    a_letters = {}
    for letter in a:
        a_letters[letter] = a_letters.get(letter, 0) + 1

    for letter in b:
        a_letters[letter] = a_letters.get(letter, 0) - 1

    return sum(map(abs, a_letters.values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
