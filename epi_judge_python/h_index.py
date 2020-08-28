from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    citations.sort()
    count = 0
    for x in reversed(citations):
        if x <= count:
            break
        count += 1

    return count


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
