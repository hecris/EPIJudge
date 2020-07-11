from typing import List

from test_framework import generic_test


# NOTE: Neat trick, A[~x] = A[-(x+1)]  = A[-1-x]
# essentially getting the corresponding back element
def rotate_matrix(square_matrix: List[List[int]]) -> None:
    def rotate_number(x, y):
        square_matrix[x][y], square_matrix[y][~x], square_matrix[~x][~y], square_matrix[~y][x] = square_matrix[~y][x], square_matrix[x][y], square_matrix[y][~x], square_matrix[~x][~y]

    lo, hi = 0, len(square_matrix) - 1
    while lo < hi:
        for i in range(lo, hi):
            rotate_number(lo, i)
        lo += 1
        hi -= 1
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
