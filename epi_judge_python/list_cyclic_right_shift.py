from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return L

    size = 1
    cur = L
    while cur.next:
        size += 1
        cur = cur.next

    k %= size
    cur.next = L
    cur = L
    for _ in range(size-k-1):
        cur = cur.next

    res, cur.next = cur.next, None
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
