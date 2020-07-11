from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    def rotate_number(x, y, lo, hi, k):
        tmp = square_matrix[x][y]
        y += k
        while y > hi:
            y -= 1
            x += 1

        tmp, square_matrix[x][y] = square_matrix[x][y], tmp

        x += k
        while x > hi:
            x -= 1
            y -= 1

        tmp, square_matrix[x][y] = square_matrix[x][y], tmp

        y -= k
        while y < lo:
            y += 1
            x -= 1

        tmp, square_matrix[x][y] = square_matrix[x][y], tmp

        x -= k
        while x < lo:
            x += 1
            y += 1

        tmp, square_matrix[x][y] = square_matrix[x][y], tmp

    lo, hi = 0, len(square_matrix) - 1
    while lo < hi:
        for i in range(lo, hi):
            rotate_number(lo, i, lo, hi, hi - lo)
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
