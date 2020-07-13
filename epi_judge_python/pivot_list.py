import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    lt = lt_tail = ListNode(0) # part less than x
    eq = eq_tail = ListNode(0) # part eq to x
    gt = gt_tail = ListNode(0) # part greater than x

    cur = l
    while cur:
        tmp = cur.next
        cur.next = None
        if cur.data < x:
            lt_tail.next = cur
            lt_tail = lt_tail.next
        elif cur.data > x:
            gt_tail.next = cur
            gt_tail = gt_tail.next
        else:
            eq_tail.next = cur
            eq_tail = eq_tail.next

        cur = tmp

    eq_tail.next = gt.next
    lt_tail.next = eq.next

    return lt.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
