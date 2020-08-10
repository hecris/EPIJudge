from typing import List

from test_framework import generic_test
from functools import lru_cache


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    r, c = len(grid), len(grid[0])
    def valid(i, j):
        return 0 <= i < r and 0 <= j < c

    @lru_cache(None)
    def solution(i, j, idx):
        if idx == len(pattern):
            return True

        if not valid(i, j) or grid[i][j] != pattern[idx]:
            return False

        adjs = [(0,1),(1,0),(0,-1),(-1,0)]
        if any(solution(i + adj[0], j + adj[1], idx+1) for adj in adjs):
            return True

        return False

    return any(solution(i, j, 0) for i in range(r)
                                 for j in range(c))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
