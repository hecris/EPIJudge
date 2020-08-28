import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    intervals.sort(key=lambda itv: (itv.left.val, not itv.left.is_closed))
    stack = []

    for interval in intervals:
        if stack and (stack[-1].right.val > interval.left.val or
                     (stack[-1].right.val == interval.left.val and (interval.left.is_closed or stack[-1].right.is_closed))):

            stack[-1] = Interval(
                    stack[-1].left,
                    max([stack[-1].right, interval.right], key = lambda p: (p.val, p.is_closed))
                    )
        else:
            stack.append(interval)

    return stack


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
