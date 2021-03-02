from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    # 10011
    # 1011
    # 111
    res = 0
    while x > 0:
        res += 1
        x &= x - 1
    return res % 2


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
