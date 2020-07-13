from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    even = even_tail = ListNode(0)
    odd = odd_tail = ListNode(0)

    cur, k = L, 0
    while cur:
        tmp = cur.next
        if k % 2:
            cur.next, odd_tail.next = None, cur
            odd_tail = odd_tail.next
        else:
            cur.next, even_tail.next = None, cur
            even_tail = even_tail.next
        cur = tmp
        k += 1

    even_tail.next = odd.next
    return even.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
