from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    carry = 0
    while L1 or L2 or carry:
        if L1:
            carry += L1.data
            L1 = L1.next
        if L2:
            carry += L2.data
            L2 = L2.next
        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry //= 10
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
