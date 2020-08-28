from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    res = []
    def solution(lo, path):
        if len(path) == k:
            res.append(path.copy())
            return
        for i in range(lo, n+1):
            path.append(i)
            solution(i+1, path)
            path.pop()

    solution(1, [])
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
