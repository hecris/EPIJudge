from typing import List

from test_framework import generic_test


# NOTE: Taken from LC - Spiral Matrix
def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    res = []
    if not square_matrix:
        return res
    r = len(square_matrix)
    c = len(square_matrix[0])
    def solution(topleft, bottomright):
        nonlocal res
        x1,y1 = topleft
        x2,y2 = bottomright
        if x1 > x2 or y1 > y2:
            return

        for i in range(x1, x2+1):
            res.append(square_matrix[y1][i])

        for i in range(y1+1, y2+1):
            res.append(square_matrix[i][x2])

        if y1 != y2:
            for i in range(x2-1,x1-1,-1):
                res.append(square_matrix[y2][i])

        if x1 != x2:
            for i in range(y2-1,y1,-1):
                res.append(square_matrix[i][x1])

        solution((topleft[0]+1,topleft[1]+1),(bottomright[0]-1,bottomright[1]-1))

    solution((0,0), (c-1,r-1))
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
