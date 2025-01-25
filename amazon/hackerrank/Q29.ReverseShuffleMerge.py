#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def reverseShuffleMerge(s):
    reverse = {} # letters needed in reverse(A)
    shuffle = {} # letters needed in shuffle(A)

    for letter in s:
        reverse[letter] = reverse.get(letter, 0) + 1
        shuffle[letter] = shuffle.get(letter, 0) + 1

    for unique_letter in reverse.keys():
        reverse[unique_letter] //= 2
        shuffle[unique_letter] //= 2

    a = []

    # s in merge(reverse(A), shuffle(A)) = reverse(s) in (A, shuffle(A))
    for letter in reversed(s):
        # Build A
        if reverse[letter] > 0:
            # Can this letter build a lexicograficaly smaller A?
            # If yes, Can we pop from A and build with shuffle(A)?
            while a and a[-1] > letter and shuffle[a[-1]] > 0:
                removed = a.pop()
                shuffle[removed] -= 1
                reverse[removed] += 1

            a.append(letter)
            reverse[letter] -= 1
        # No other option, take from shuffle
        else:
            shuffle[letter] -= 1

    return "".join(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
