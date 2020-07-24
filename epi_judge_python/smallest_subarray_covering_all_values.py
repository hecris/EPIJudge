import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


# NOTE: struggled with this
def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:
    keyword_idx = {x: i for i, x in enumerate(keywords)}
    last_occur = [-1] * len(keywords)
    shortest_sub = [float('inf')] * len(keywords)

    ans = None
    for i, word in enumerate(paragraph):
        if word not in keyword_idx:
            continue

        idx = keyword_idx[word]
        if idx == 0:
            shortest_sub[idx] = 1
        elif shortest_sub[idx - 1] != float('inf'):
            distance = i - last_occur[idx - 1]
            shortest_sub[idx] = shortest_sub[idx - 1] + distance

        last_occur[idx] = i

        if idx == len(keywords) - 1:
            if not ans or shortest_sub[-1] < ans.end - ans.start + 1:
                ans = Subarray(i - shortest_sub[-1] + 1, i)

    return ans


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure('Not all keywords are in the generated subarray')
        if para_idx >= len(paragraph):
            raise TestFailure('Subarray end index exceeds array size')
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_all_values.py',
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
