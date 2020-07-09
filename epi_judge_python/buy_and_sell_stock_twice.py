from typing import List

from test_framework import generic_test


# NOTE: consider iterating backwards to solve array problems
def buy_and_sell_stock_twice(prices: List[float]) -> float:
    before = []
    msf, profit = float('inf'), 0
    for i in range(len(prices)):
        profit = max(profit, prices[i] - msf)
        before.append(profit)
        msf = min(msf, prices[i])

    msf, profit = float('-inf'), 0
    after = [0] * len(prices)
    for i in reversed(range(len(prices))):
        profit = max(profit, msf - prices[i])
        after[i] = profit
        msf = max(msf, prices[i])

    res = 0
    for i in range(len(prices)):
        res = max(res, (before[i-1] if i > 0 else 0) + after[i])

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
