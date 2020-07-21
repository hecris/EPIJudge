from test_framework import generic_test
import math


def square_root(x: float) -> float:
    lo, hi = (0,1) if x < 1 else (1, x)

    while not math.isclose(lo,hi):
        mid = (lo + hi) * 0.5
        sq = mid * mid
        if x < sq:
            hi = mid
        else:
            lo = mid

    return lo


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
