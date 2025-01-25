#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
# Function to find the median using the counting sort technique
def find_median(counts, d):
    count_sum = 0
    median1 = None
    median2 = None

    if d % 2 == 1:
        median_position = d // 2 + 1
    else:
        median_position = d // 2

    for idx, count in enumerate(counts):
        count_sum += count
        if median1 is None and count_sum >= median_position:
            median1 = idx
        if count_sum >= median_position + 1:
            median2 = idx
            break

    return median1 if d % 2 == 1 else (median1 + median2) / 2

def activityNotifications(expenditure, d):
    notices = 0
    counts = [0 for _ in range(max(expenditure) + 1)]

    for val in expenditure[:d]:
        counts[val] += 1

    for idx in range(d, len(expenditure)):
        median = find_median(counts, d)
        if expenditure[idx] >= 2 * median:
            notices += 1

        counts[expenditure[idx - d]] -= 1
        counts[expenditure[idx]] += 1

    return notices

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
