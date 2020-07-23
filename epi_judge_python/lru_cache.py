from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import OrderedDict


# NOTE: cool solution using OrderedDict, normally use queue + hashmap
class LruCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.items = OrderedDict()

    def lookup(self, isbn: int) -> int:
        if isbn not in self.items:
            return -1
        ans = self.items.pop(isbn)
        self.items[isbn] = ans
        return ans

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.items:
            price = self.items.pop(isbn)
        elif len(self.items) == self.capacity:
            self.items.popitem(last=False)

        self.items[isbn] = price

    def erase(self, isbn: int) -> bool:
        return self.items.pop(isbn, None) is not None


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    # l = LruCache(3)
    # l.insert(1,2)
    # l.insert(3,4)
    # l.insert(5,6)
    # l.lookup(1)
    # l.insert(7,8)
    # print(l.items)
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
