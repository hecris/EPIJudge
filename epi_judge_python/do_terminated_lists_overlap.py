import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def len_and_tail(head):
        length = 1
        while head.next:
            length += 1
            head = head.next
        return length, head

    dummy1, dummy2 = ListNode(0, l0), ListNode(0, l1)
    len1, tail1 = len_and_tail(dummy1)
    len2, tail2 = len_and_tail(dummy2)

    if tail1 is not tail2:
        return None

    diff = abs(len1 - len2)
    if len1 > len2:
        for _ in range(diff):
            dummy1 = dummy1.next
    else:
        for _ in range(diff):
            dummy2 = dummy2.next

    while dummy1 is not dummy2:
        dummy1, dummy2 = dummy1.next, dummy2.next

    return dummy1


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
