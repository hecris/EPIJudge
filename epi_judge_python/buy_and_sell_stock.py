from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_so_far = prices[0]
    res = 0
    for p in prices[1:]:
        res = max(res, p - min_so_far)
        min_so_far = min(min_so_far, p)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
