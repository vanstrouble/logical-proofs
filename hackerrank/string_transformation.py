#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#


def transformSentence(sentence):
    # Write your code here
    words = sentence.split()
    result = []
    for word in words:
        speech = word[0]
        for i in range(1, len(word)):
            prev_c = word[i-1]
            c = word[i]

            if prev_c.lower() < c.lower():
                speech += c.upper()
            elif prev_c.lower() > c.lower():
                speech += c.lower()
            else:
                speech += c

        result.append(speech)
    return ' '.join(result)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
