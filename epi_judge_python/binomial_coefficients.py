from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    memo = {}
    def choose(n, k):
        if k > n or k < 0: return 0
        if n == 1: return 1
        if not (n, k) in memo:
            memo[n,k] = choose(n-1, k-1) + choose(n-1, k)
        return memo[n, k]

    return choose(n, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
