from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    stack = []
    for i in range(len(sequence)):
        while stack and sequence[stack[-1]] <= sequence[i]:
            stack.pop()
        stack.append(i)
    stack.reverse()
    return stack


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
