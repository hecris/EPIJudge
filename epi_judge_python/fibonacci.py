from test_framework import generic_test
from functools import lru_cache


@lru_cache(None)
def fibonacci(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
