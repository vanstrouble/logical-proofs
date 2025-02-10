"""
Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

Example:
move_zeros([0, 1, 2, 0, 3]) # returns [1, 2, 3, 0, 0]
"""


def move_zeros(lst):
    return sorted(lst, key=lambda x: x == 0)


if __name__ == '__main__':
    print(move_zeros([0, 1, 2, 0, 3]))  # [1, 2, 3, 0, 0]
    print(move_zeros([0, 0, 0, 0, 0]))  # [0, 0, 0, 0, 0]
    print(move_zeros([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
    print(move_zeros([0, 0, 1, 0]))  # [1, 0, 0, 0]
    print(move_zeros([0, 0, 1, 0, 0]))  # [1, 0, 0, 0, 0]
