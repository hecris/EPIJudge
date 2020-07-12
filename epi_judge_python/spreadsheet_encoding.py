from test_framework import generic_test
import functools


def ss_decode_col_id(col: str) -> int:
    mymap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # res = 0
    # for i in range(len(col)):
    #     res *= 26
    #     res += mymap.index(col[i]) + 1
    # return res
    # pythonic one line solution
    return functools.reduce(lambda running_sum, digit: running_sum * 26 + mymap.index(digit) + 1, col, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
