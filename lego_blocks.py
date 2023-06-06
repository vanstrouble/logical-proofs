''''
You have an infinite number of 4 types of lego blocks of sizes given as (depth x height x width):
d	h	w
1	1	1
1	1	2
1	1	3
1	1	4
Using these blocks, you want to make a wall of height n and width m. Features of the wall are: 

- The wall should not have any holes in it. 
- The wall you build should be one solid structure, so there should not be a straight vertical break across all rows of bricks. 
- The bricks must be laid horizontally.
How many ways can the wall be built?
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    MOD = 10**9 + 7

    singleCombo = [1, 2, 4, 8]
    for i in range(4, m):
        singleCombo.append(sum(singleCombo[-4:]) % MOD)

    totalCombo = [(row**n) % MOD for row in singleCombo]

    validCombo = [1]

    for i in range(1, m):
        invalidCombo = sum([total * valid for total, valid in zip(totalCombo[:i], validCombo[::-1])])
        validCombo.append((totalCombo[i] - invalidCombo) % MOD)

    return validCombo[-1]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
