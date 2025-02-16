#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    if s == s[::-1]:
        return -1
    
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if s[i + 1:n - i] == s[i + 1:n - i][::-1]:
                return i
            else:
                return n - i - 1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
