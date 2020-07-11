from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    res = []
    negative = False
    if x < 0:
        negative = True
        x *= -1

    while True:
        digit = x % 10
        x //= 10
        res.append(chr(digit + 48))
        if x == 0:
            break

    if negative:
        res.append('-')

    res.reverse()
    return ''.join(res)


def string_to_int(s: str) -> int:
    res = 0
    sign = 1
    for i in (range(len(s))):
        if s[i] == '-':
            sign = -1
            continue
        if s[i] == '+':
            continue
        digit = ord(s[i]) - 48
        res *= 10
        res += digit
    return res * sign


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    # print(string_to_int("0"))
    # print(int_to_string(0))
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
