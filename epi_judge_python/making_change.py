from test_framework import generic_test


def change_making(cents: int) -> int:
    coins = [100, 50, 25, 10, 5, 1]
    ans = 0
    for coin in coins:
        ans += cents // coin
        cents %= coin
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('making_change.py', 'making_change.tsv',
                                       change_making))
