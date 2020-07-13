from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not L or start == finish:
        return L

    def kth_node(head, k):
        for i in range(k):
            head = head.next
        return head

    def reverse(head):
        if not head:
            return
        p1 = None
        p2 = head
        while p2:
            p2.next, p1, p2 = p1, p2, p2.next

        return p1

    dummy_head = ListNode(0, L)

    reverse_head = kth_node(dummy_head, start - 1)
    reverse_tail = kth_node(dummy_head, finish)

    tmp, reverse_head.next = reverse_head.next, None
    tmp2, reverse_tail.next = reverse_tail.next, None

    new_head = reverse(tmp)
    reverse_head.next = new_head
    tmp.next = tmp2
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
