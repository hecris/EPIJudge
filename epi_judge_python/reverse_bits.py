from test_framework import generic_test


def reverse_bits(x: int) -> int:
    res = 0
    leading_zeroes = 64
    while x > 0:
        last_bit = x & 1
        res <<= 1
        res += last_bit
        x >>= 1
        leading_zeroes -= 1

    while leading_zeroes > 0:
        res <<= 1
        leading_zeroes -= 1

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
