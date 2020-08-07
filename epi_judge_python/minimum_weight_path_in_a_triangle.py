from typing import List

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:
    if not triangle: return 0

    n = len(triangle)
    # NOTE: can be optimized by only storing most recent row
    dp = [[0] * (i+1) for i in range(n)]
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i+1):
            dp[i][j] = triangle[i][j] + min(
                    dp[i-1][j] if j != i else float('inf'),
                    dp[i-1][j-1] if j >= 1 else float('inf')
                    )

    return min(dp[n-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
