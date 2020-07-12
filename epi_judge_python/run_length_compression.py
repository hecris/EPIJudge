from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    i = 0
    res = []
    while i < len(s):
        num = ''
        while s[i].isnumeric():
            num += s[i]
            i += 1
        res.append(s[i] * int(num))
        i += 1
    return ''.join(res)


def encoding(s: str) -> str:
    i = 0
    res = []
    while i < len(s):
        count = 1
        while i < len(s) - 1 and s[i] == s[i+1]:
            count += 1
            i += 1
        res.append(str(count) + s[i])
        i += 1
    return ''.join(res)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
