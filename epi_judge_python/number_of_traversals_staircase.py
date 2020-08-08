from test_framework import generic_test


def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    dp = [0] * (top + 1)
    dp[0] = 1
    for i in range(1, top+1):
        for j in range(1, maximum_step+1):
            if i - j >= 0:
                dp[i] += dp[i-j]
    return dp[top]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
