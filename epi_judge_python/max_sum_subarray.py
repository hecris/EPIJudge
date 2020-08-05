from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    dp = [0] * len(A)
    for i in range(len(A)):
        if i == 0:
            dp[i] = max(0, A[0])
        else:
            dp[i] = max(A[i], dp[i-1] + A[i])
    return max(dp) if dp else 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
