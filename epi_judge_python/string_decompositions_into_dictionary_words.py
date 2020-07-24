from typing import List

from test_framework import generic_test
from collections import Counter


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    w = Counter(words)
    k = len(words[0])
    target_length = len(words) * k

    res = []
    def helper(lo):
        word_counter = w.copy()
        hi = lo
        while hi < len(s):
            next_word = s[hi:hi+k]
            if next_word not in word_counter:
                hi += k
                while lo < hi:
                    lo_word = s[lo:lo+k]
                    if lo_word in word_counter:
                        word_counter[lo_word] += 1
                    lo += k
            elif word_counter[next_word] == 0:
                while word_counter[next_word] == 0:
                    lo_word = s[lo:lo+k]
                    if lo_word in word_counter:
                        word_counter[lo_word] += 1
                    lo += k
            elif hi + k - lo == target_length:
                res.append(lo)
                lo_word = s[lo:lo+k]
                word_counter[lo_word] += 1
                lo += k
            else:
                word_counter[next_word] -= 1
                hi += k

    for i in range(k):
        helper(i)

    return sorted(res)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
