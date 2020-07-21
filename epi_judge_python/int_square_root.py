from test_framework import generic_test


def square_root(k: int) -> int:
    lo, hi = 0, k
    # think of this terminating statement as an empty interval.
    # that is, the terminal is empty iff lo > hi
    while lo <= hi:
        mid = (lo + hi) // 2
        sq = mid * mid
        if sq <= k:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
