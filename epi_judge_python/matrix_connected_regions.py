from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    r, c = len(image), len(image[0])
    def valid(x,y):
        return x >= 0 and x < r and y >= 0 and y < c

    color = image[x][y]
    def dfs(x,y):
        if not valid(x,y) or image[x][y] != color:
            return
        image[x][y] = not color
        for x2, y2 in [(0,1),(1,0),(-1,0),(0,-1)]:
            dfs(x+x2, y+y2)
    dfs(x,y)
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
