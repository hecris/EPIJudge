from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L:
        return True

    def reverse(head):
        prev = None
        cur = head
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        return prev

    slow = fast = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    tmp, slow.next = slow.next, None
    tmp = reverse(tmp)
    while L and tmp:
        if L.data != tmp.data:
            return False
        L, tmp = L.next, tmp.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
