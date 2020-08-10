from test_framework import generic_test
from functools import lru_cache


def levenshtein_distance(A: str, B: str) -> int:
    n, m = len(A), len(B)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i

    for j in range(m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1],
                                   dp[i-1][j],
                                   dp[i][j-1])

    return dp[n][m]

    @lru_cache(None)
    def solution(i, j):
        if i == len(A) and j == len(B):
            return 0

        if i == len(A):
            return len(B) - j

        if j == len(B):
            return len(A) - i

        if A[i] == B[j]:
            return solution(i+1, j+1)

        return 1 + min(solution(i+1, j+1),
                       solution(i+1, j),
                       solution(i, j+1))
    return solution(0, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
