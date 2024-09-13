#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING input_str as parameter.


def getString(input_str):
    # Write your code here
    count = {}

    for c in input_str:
        count[c] = count.get(c, 0) + 1

    stack = []

    for c in input_str:
        count[c] -= 1

        if c in stack:
            continue

        while stack and c > stack[-1] and count[stack[-1]] > 0:
            stack.pop()

        stack.append(c)

    return ''.join(stack)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input_str = input()

    result = getString(input_str)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
