from test_framework import generic_test
import functools


def roman_to_integer(s: str) -> int:
    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

    # Pythonic one liner
    # return functools.reduce(
    #         lambda val, i: val + (-roman[s[i]] if roman[s[i]] < roman[s[i+1]] else roman[s[i]]),
    #         reversed(range(len(s) - 1)),
    #         roman[s[-1]])

    i = 0
    res = 0
    while i < len(s) - 1:
        cur = s[i]
        next = s[i + 1]
        if roman[next] > roman[cur]:
            res += roman[next] - roman[cur]
            i += 2
        else:
            res += roman[cur]
            i += 1

    if i == len(s) - 1:
        res += roman[s[-1]]

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
