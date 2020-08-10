import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    n = len(items)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n)]

    for w in range(1, capacity+1):
        if items[0].weight <= w:
            dp[0][w] = items[0].value

    for i in range(1, n):
        item = items[i]
        for w in range(1, capacity+1):
            dp[i][w] = dp[i-1][w]
            if w - item.weight >= 0:
                dp[i][w] = max(dp[i][w],
                               dp[i-1][w-item.weight] + item.value)

    return dp[n-1][capacity]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
