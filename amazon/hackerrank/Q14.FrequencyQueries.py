#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    value_count = {}
    ocurrence_count = {}
    ans = []

    for query_type, value in queries:
	if query_type == 1:
            prev_count = value_count.get(value, 0)
            new_count = prev_count + 1

            value_count[value] = new_count

            if prev_count > 0:
                ocurrence_count[prev_count] -= 1
            ocurrence_count[new_count] = ocurrence_count.get(new_count, 0) + 1

        elif query_type == 2:
            if value_count.get(value, 0) <= 0:
                continue

            prev_count = value_count[value]
            new_count = prev_count - 1

            value_count[value] = new_count

            if new_count > 0:
                ocurrence_count[new_count] = ocurrence_count.get(new_count, 0) + 1
            ocurrence_count[prev_count] -= 1

        else:
            ans.append(1 if ocurrence_count.get(value, 0) > 0 else 0)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
