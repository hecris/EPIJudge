from typing import List

from test_framework import generic_test
from collections import Counter, defaultdict


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    required = Counter(words)
    k = len(words[0])
    target_length = len(words) * k

    res = []
    def helper(lo):
        curr = defaultdict(int)
        hi = lo
        while hi < len(s):
            next_word = s[hi:hi+k]
            if next_word not in required:
                hi += k
                while lo < hi:
                    lo_word = s[lo:lo+k]
                    if lo_word in curr:
                        curr[lo_word] -= 1
                    lo += k
            elif required[next_word] == curr[next_word]:
                while curr[next_word] == required[next_word]:
                    lo_word = s[lo:lo+k]
                    if lo_word in curr:
                        curr[lo_word] -= 1
                    lo += k
            elif hi + k - lo == target_length:
                res.append(lo)
                lo_word = s[lo:lo+k]
                curr[lo_word] -= 1
                lo += k
            else:
                curr[next_word] += 1
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
