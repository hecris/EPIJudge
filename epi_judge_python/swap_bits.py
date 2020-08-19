from test_framework import generic_test


def swap_bits(x, i, j):
    i_mask = 1 << i
    j_mask = 1 << j
    i_bit = x & i_mask
    j_bit = x & j_mask

    if (i_bit or j_bit) and (not i_bit or not j_bit):
        x ^= i_mask
        x ^= j_mask

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
