from test_framework import generic_test


def divide(x: int, y: int) -> int:
    quotient = 0
    k = 32
    y_2k = y << k

    while x >= y:
        while y_2k > x:
            y_2k >>= 1
            k -= 1
        x -= y_2k
        quotient += (1 << k)

    return quotient


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
