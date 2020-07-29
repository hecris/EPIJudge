from typing import List

from test_framework import generic_test, test_utils
import math


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    # NOTE: use bijections between integers, bit arrays of length n, and power set of a set of length n
    def iterative(input_set):
        power_set = []
        for i in range(1 << len(input_set)):
            subset = []
            while i:
                leftmost_set_bit = i & ~(i - 1)
                index = int(math.log2(leftmost_set_bit))
                subset.append(input_set[index])
                i &= i - 1
            power_set.append(subset)

        return power_set

    return iterative(input_set)

    res = []
    def solution(lo, path):
        res.append(path.copy())

        for i in range(lo, len(input_set)):
            path.append(input_set[i])
            solution(i+1, path)
            path.pop()


    solution(0, [])
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
