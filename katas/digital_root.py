"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.

Examples:
16  -->  1 + 6 = 7
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""


def digital_root(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n


# Other Solutions:

# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))

# def digital_root(n):
#     return n%9 or n and 9

# def digital_root(n):
#     return (n - 1) % 9 + 1 if n != 0 else 0


if __name__ == '__main__':
    print(digital_root(8))
    print(digital_root(16))
    print(digital_root(942))
    print(digital_root(132189))
    print(digital_root(493193))
