from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    isprime = [True] * (n+1)
    isprime[0] = isprime[1] = False
    i = 2
    while i <= n:
        if isprime[i]:
            j = i + i
            while j <= n:
                isprime[j] = False
                j += i
        i += 1

    return [i for i, x in enumerate(isprime) if x]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
