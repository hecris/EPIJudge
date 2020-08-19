from test_framework import generic_test


def reverse(x: int) -> int:
    negative = False
    if x < 0:
        negative = True

    x = abs(x)
    res = 0
    while x != 0:
        digit = x % 10
        x //= 10
        res = (res * 10) + digit

    return -res if negative else res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
