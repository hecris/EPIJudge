from typing import List

from test_framework import generic_test


def fill_surrounded_regions(board: List[List[str]]) -> None:
    r,c = len(board), len(board[0])
    def valid(x,y):
        return x >= 0 and x < r and y >= 0 and y < c

    not_enclosed = set() # NOTE: can do this in constant space
    def dfs(x,y):
        if not valid(x,y) or (x,y) in not_enclosed or board[x][y] == 'B':
            return
        not_enclosed.add((x,y))
        for x2, y2 in [(0,1),(1,0),(-1,0),(0,-1)]:
            dfs(x+x2,y+y2)

    for i in range(r):
        dfs(i, 0)
        dfs(i, c-1)

    for j in range(c):
        dfs(0, j)
        dfs(r-1, j)

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'W' and (i,j) not in not_enclosed:
                board[i][j] = 'B'

    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
