from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    def solution(lo, path):
        if lo == len(text):
            res.append(path.copy())
            return

        for i in range(lo+1, len(text) + 1):
            prefix = text[lo:i]
            if prefix == prefix[::-1]:
                solution(i, path + [prefix])

    res = []
    solution(0, [])
    return res

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
