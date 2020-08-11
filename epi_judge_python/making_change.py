from test_framework import generic_test


def change_making(cents: int) -> int:
    coins = [1, 5, 10, 25, 50, 100]
    ans = 0
    while cents:
        while coins[-1] > cents:
            coins.pop()
        cents -= coins[-1]
        ans += 1

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('making_change.py', 'making_change.tsv',
                                       change_making))
