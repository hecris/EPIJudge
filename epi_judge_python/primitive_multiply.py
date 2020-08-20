from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    def add(a,b):
        while b:
            carry = a & b
            a ^= b
            b = carry << 1
        return a

    ans = 0
    i = 0
    while y:
        if y & 1:
            ans = add(ans, x << i)
        # alternatively, x <<= 1
        i += 1
        y >>= 1
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
