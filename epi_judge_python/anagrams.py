from typing import List

from test_framework import generic_test, test_utils
from collections import defaultdict


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    def get_counter(word):
        counter = [0] * 26
        for char in word:
            if char == ' ':
                continue
            counter[ord(char) - ord('a')] += 1
        return tuple(counter)

    d = defaultdict(list)
    for word in dictionary:
        d[get_counter(word)].append(word)

    return [group for group in d.values() if len(group) > 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
