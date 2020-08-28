from typing import List

from test_framework import generic_test


def calculate_largest_rectangle(heights: List[int]) -> int:
    n = len(heights)
    l = [0] * n
    r = [0] * n
    stack = []
    for i, x in enumerate(heights):
        if not stack or x >= heights[stack[-1]]:
            if stack:
                l[i] = stack[-1] + 1
            stack.append(i)
        else:
            while stack and x < heights[stack[-1]]:
                idx = stack.pop()
                if stack:
                    l[idx] = stack[-1] + 1
                r[idx] = i - 1
            stack.append(i)

    while stack:
        idx = stack.pop()
        if stack:
            l[idx] = stack[-1] + 1
        r[idx] = i

    max_area = 0
    for i in range(n):
        area = heights[i] * (r[i] - l[i] + 1)
        max_area = max(max_area, area)

    return max_area

    # suboptimal divide and conquer solution
    # worst case O(N^2)
    def solution(lo, hi):
        if lo > hi: return 0
        if lo == hi: return heights[lo]

        min_idx = min((i for i in range(lo, hi+1)), key= lambda idx: heights[idx])
        left = solution(lo, min_idx-1)
        right = solution(min_idx+1, hi)
        return max(left, right, heights[min_idx] * (hi - lo + 1))

    return solution(0, len(heights)-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
