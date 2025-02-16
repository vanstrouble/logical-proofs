"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)
"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
"""

# My solution
# def is_isogram(string):
#     if not string:
#         return True
#     string = string.lower()
#     for char in string:
#         if string.count(char) > 1:
#             return False
#     return True


# Another solution
def is_isogram(string):
    return len(string) == len(set(string.lower()))


if __name__ == "__main__":
    print(is_isogram("Dermatoglyphics"))  # True
    print(is_isogram("aba"))  # False
    print(is_isogram("moOse"))  # False
    print(is_isogram(""))  # True
    print(is_isogram("a"))  # True
    print(is_isogram("ab"))  # True
    print(is_isogram("abc"))  # True
    print(is_isogram("abcabc"))  # False
    print(is_isogram("abcabcabc"))  # False
