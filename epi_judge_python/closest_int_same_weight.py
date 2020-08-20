from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    for i in range(63):
        this_mask = (1 << i)
        next_mask = (1 << (i+1))
        if (x & this_mask and x & next_mask) or not (x & this_mask or x & next_mask):
            continue

        x ^= this_mask | next_mask
        return x

    raise ValueError('All bits are 0 or 1')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
