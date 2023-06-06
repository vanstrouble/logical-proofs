#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = []
    opening = "({["
    closing = ")}]"

    for c in s:
        if c in opening:
            stack.append(c)
        elif c in closing:
            if not stack:
                return 'NO'
            last_open = stack.pop()
            if opening.index(last_open) != closing.index(c):
                return 'NO'
    return 'YES' if not stack else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
