from typing import List

from test_framework import generic_test


def minimum_messiness(words: List[str], line_length: int) -> int:
    from functools import lru_cache
    @lru_cache(None)
    def solution(idx):
        if idx == len(words):
            return 0
        mymin = float('inf')
        myline = 0
        for i in range(idx, len(words)):
            myline += len(words[i])
            diff = line_length - myline
            if diff < 0:
                break
            mymin = min(mymin, diff * diff + solution(i+1))
            myline += 1
        return mymin

    return solution(0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
