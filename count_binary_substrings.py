#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getSubstringCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getSubstringCount(s):
    # Write your code here
    count = 0
    temp = 0
    curr = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr += 1
        else:
            count += min(temp, curr)
            temp = curr
            curr = 1

    count += min(temp, curr)

    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getSubstringCount(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(result)
