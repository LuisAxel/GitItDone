#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    letters = {}
    for letter in s:
        letters[letter] = letters.get(letter, 0) + 1

    frequencies = {}
    for frequency in letters.values():
        frequencies[frequency] = frequencies.get(frequency, 0) + 1

    frequencies_n = len(frequencies)
    if frequencies_n == 1:
        return "YES"
    if frequencies_n > 2:
        return "NO"

    count1, count2 = frequencies.values()
    frequency1, frequency2 = frequencies.keys()

    # Ensure freq2 is bigger frequency
    if frequency1 >= frequency2:
        frequency1, frequency2 = frequency2, frequency1
        count1, count2 = count2, count1

    if frequency1 == 1 and count1 == 1:
        return "YES"
    if frequency2 - frequency1 == 1 and count2 == 1:
        return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
