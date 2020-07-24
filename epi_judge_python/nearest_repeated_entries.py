from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    d = {}
    ans = float('inf')

    for i, word in enumerate(paragraph):
        if word in d:
            ans = min(ans, i - d[word])
        d[word] = i

    return ans if ans != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
