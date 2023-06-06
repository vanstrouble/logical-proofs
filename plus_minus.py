#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0
    
    n = 0
    for number in arr:
        n += 1
        if (number > 0):
            positives += 1
        elif (number < 0):
            negatives += 1
        else:
            zeros += 1
    
    positives_ratio = round(positives / n, 6)
    negatives_ratio = round(negatives / n, 6)
    zeros_ratio = round(zeros / n, 6)

    print(f"{positives_ratio}")
    print(f"{negatives_ratio}")
    print(f"{zeros_ratio}")
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
