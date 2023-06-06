#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    encrypted = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) - 65 + k) % 26 + 65)
            else:
                encrypted += chr((ord(char) - 97 + k) % 26 + 97)
        else:
            encrypted += char
    return encrypted

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(f"{result}")

    # fptr.write(result + '\n')

    # fptr.close()
