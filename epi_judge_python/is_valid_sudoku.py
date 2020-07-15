from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
import math
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(partial_assignment)
    if any(
            has_duplicate([partial_assignment[i][j] for j in range(n)]) or
            has_duplicate([partial_assignment[j][i] for j in range(n)])
            for i in range(n)):
        return False

    region = int(math.sqrt(n))
    return all(
            not has_duplicate([partial_assignment[i][j]
                for i in range(x, x+region)
                for j in range(y, y+region)])
            for y in range(0, n, region) for x in range(0, n, region))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
