from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    fast = L
    for _ in range(k+1):
        if not fast:
            # we are deleting the head
            return L.next
        fast = fast.next

    slow = L
    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
