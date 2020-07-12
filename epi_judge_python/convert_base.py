from test_framework import generic_test
import string
import functools


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    def convert_to_s(num_as_int, base):
        res = []
        while True:
            digit = num_as_int % base
            num_as_int //= base
            res.append(string.hexdigits[digit].upper())
            if num_as_int == 0:
                break
        res.reverse()
        return ''.join(res)

    negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(
            lambda running_sum, c: running_sum * b1 + string.hexdigits.index(c.lower()),
            num_as_string[negative:], 0)
    return ('-' if negative else '') + convert_to_s(num_as_int, b2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
