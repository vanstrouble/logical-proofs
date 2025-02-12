"""
Write a function that takes an integer as input,
and returns the number of bits that are equal to one
in the binary representation of that number.

You can guarantee that input is non-negative.

Example:
The binary representation of 1234 is 10011010010,
so the function should return 5 in this case.
"""


def count_bits(n):
    return bin(n).count('1')


if __name__ == '__main__':
    print(count_bits(1234))
    print(count_bits(4))
    print(count_bits(7))
    print(count_bits(9))
    print(count_bits(10))
