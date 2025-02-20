#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    magazine_words = {}

    for word in magazine:
        magazine_words[word] = magazine_words.get(word, 0) + 1

    for word in note:
        if magazine_words.get(word, 0) == 0:
            print("No")
            return
        magazine_words[word] -= 1

    print("Yes")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
