from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = ((dp[i-1][j] if i >= 1 else 0)
                           +(dp[i][j-1] if j >= 1 else 0))

    return dp[n-1][m-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
