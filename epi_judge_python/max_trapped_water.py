from typing import List

from test_framework import generic_test


def get_max_trapped_water(heights: List[int]) -> int:
    lo, hi = 0, len(heights) - 1
    ans = 0
    while lo < hi:
        area = min(heights[lo], heights[hi]) * (hi - lo)
        ans = max(ans, area)
        if heights[lo] == heights[hi]:
            lo += 1
            hi -= 1
        elif heights[lo] < heights[hi]:
            lo += 1
        else:
            hi -= 1
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
