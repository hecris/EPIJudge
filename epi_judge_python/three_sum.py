from typing import List

from test_framework import generic_test

def has_three_sum(A: List[int], t: int) -> bool:
    def two(lo, target):
        hi = len(A) - 1
        while lo <= hi:
            mysum = A[lo] + A[hi]
            if mysum == target:
                return True
            elif mysum < target:
                lo += 1
            else:
                hi -= 1
        return False

    A.sort()
    return any(two(i, t - x) for i, x in enumerate(A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
