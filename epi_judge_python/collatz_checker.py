from test_framework import generic_test


def test_collatz_conjecture(n: int) -> bool:
    verified = set()
    for i in range(3,n+1,2):
        seen = set()
        cur = i
        while cur >= i:
            if cur in seen:
                return False
            seen.add(cur)

            if cur % 2:
                if cur in verified:
                    break
                verified.add(cur)
                cur = (cur * 3) + 1
            else:
                cur //= 2

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
