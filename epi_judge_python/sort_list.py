from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next

def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    def solution(head):
        if not head or not head.next:
            return head

        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        half = prev.next
        prev.next = None

        left = solution(head)
        right = solution(half)
        return merge_two_sorted_lists(left, right)

    return solution(L)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
