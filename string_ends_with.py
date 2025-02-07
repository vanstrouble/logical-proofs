"""
Complete the solution so that it returns true if the first argument (string)
passed in ends with the 2nd argument (also a string).

Examples:
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""


def solution(text, ending):
    return text.endswith(ending)


if __name__ == '__main__':
    print(solution('abc', 'bc'))
    print(solution('abc', 'd'))
    print(solution('samurai', 'ai'))
    print(solution('ninja', 'ja'))
    print(solution('sensei', 'i'))
    print(solution('sumo', 'omo'))
    print(solution('samurai', 'ra'))
    print(solution('abc', 'abcd'))
    print(solution('ails', 'fails'))
