from test_framework import generic_test
from test_framework.test_failure import TestFailure
import bintrees


class ClientsCreditsInfo:
    def __init__(self):
        self.inc = 0
        self.client_to_credit = {}
        self.credits_to_client = bintrees.RBTree()

    def insert(self, client_id: str, c: int) -> None:
        self.client_to_credit[client_id] = c - self.inc
        self.credits_to_client.setdefault(c - self.inc, set())
        self.credits_to_client[c - self.inc].add(client_id)

    def remove(self, client_id: str) -> bool:
        if client_id not in self.client_to_credit:
            return False
        credit = self.client_to_credit.pop(client_id)
        self.credits_to_client[credit].remove(client_id)
        if not self.credits_to_client[credit]:
            self.credits_to_client.pop(credit)
        return True

    def lookup(self, client_id: str) -> int:
        if client_id not in self.client_to_credit:
            return -1
        return self.client_to_credit[client_id] + self.inc

    def add_all(self, C: int) -> None:
        self.inc += C

    def max(self) -> str:
        return self.credits_to_client.max_item()[1][0]


def client_credits_info_tester(ops):
    cr = ClientsCreditsInfo()

    for x in ops:
        op = x[0]
        s_arg = x[1]
        i_arg = x[2]
        if op == 'ClientsCreditsInfo':
            pass
        if op == 'max':
            result = cr.max()
            if result != s_arg:
                raise TestFailure('Max: return value mismatch')
        elif op == 'remove':
            result = cr.remove(s_arg)
            if result != i_arg:
                raise TestFailure('Remove: return value mismatch')
        elif op == 'insert':
            cr.insert(s_arg, i_arg)
        elif op == 'add_all':
            cr.add_all(i_arg)
        elif op == 'lookup':
            result = cr.lookup(s_arg)
            if result != i_arg:
                raise TestFailure('Lookup: return value mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('adding_credits.py',
                                       'adding_credits.tsv',
                                       client_credits_info_tester))
