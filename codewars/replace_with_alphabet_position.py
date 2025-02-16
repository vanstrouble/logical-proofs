"""
Replace With Alphabet Position

In this kata you are required to, given a string, replace every letter with its position in the
alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example:
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
"""


def alphabet_position(text):
    return " ".join(str(ord(char) - 96) for char in text.lower() if char.isalpha())


if __name__ == "__main__":
    print(alphabet_position("Regina Guerrero is my girlfriend."))
    print(alphabet_position("The sunset sets at twelve o' clock."))
    print(alphabet_position("The narwhal bacons at midnight."))
