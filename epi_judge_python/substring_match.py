from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    import functools

    if len(s) == 0: # edge case
        return 0

    BASE = 128 # printable ascii characters, NOTE: doesn't seem to matter
    t_hash = functools.reduce(lambda value, c: value * BASE + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda value, c: value * BASE + ord(c), s, 0)
    power = BASE ** (len(s) - 1)

    lo, hi = 0, len(s)
    while hi < len(t):
        if t_hash == s_hash and t[lo:hi] == s:
            return lo
        t_hash -= ord(t[lo]) * power
        t_hash = t_hash * BASE + ord(t[hi])
        lo += 1
        hi += 1

    if t_hash == s_hash and t[lo:hi] == s:
        return lo

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
