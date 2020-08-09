from typing import List

from test_framework import generic_test


def maximum_revenue(coins: List[int]) -> int:
    if len(coins) == 1: return coins[0]
    memo = {}
    def solution(i, j, mysum):
        if i > j:
            return 0

        if (i, j) not in memo:
            first = solution(i+1, j, mysum - coins[i])
            last = solution(i, j-1, mysum - coins[j])

            ans = mysum - last
            if first < last:
                ans = mysum - first
            memo[i,j] = ans

        return memo[i, j]

    return solution(0, len(coins) - 1, sum(coins))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
