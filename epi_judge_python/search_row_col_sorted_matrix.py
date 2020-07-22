from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    target = x
    x, y = 0, len(A[0]) - 1
    while x < len(A) and y >= 0:
        if A[x][y] == target:
            return True
        elif A[x][y] < target:
            x += 1
        else:
            y -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
