import collections
import functools
from typing import List
import heapq

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    # def alternate(A):
    #     # 0 for is starting point
    #     E = [point for event in A for point in ((event.start, 0), (event.finish, 1))]
    #     E.sort()
    #     max_concurrent = 0
    #     cur_concurrent = 0
    #     for point, is_start in E:
    #         if is_start == 0:
    #             cur_concurrent += 1
    #         else:
    #             cur_concurrent -= 1

    #         max_concurrent = max(max_concurrent, cur_concurrent)

    #     return max_concurrent

    # return alternate(A)
    A.sort()
    heap = []
    res = 0
    for event in A:
        while heap and heap[0] < event.start:
            heapq.heappop(heap)

        heapq.heappush(heap, event.finish)
        res = max(res, len(heap))

    return res


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
