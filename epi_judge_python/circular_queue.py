from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.array = [0] * capacity
        self.head = self.tail = self.num_items = 0
        return

    def enqueue(self, x: int) -> None:
        if self.num_items == len(self.array):
            self.array = self.array[self.head:] + self.array[:self.head]
            self.head, self.tail = 0, self.num_items
            self.array += [0] * len(self.array)
        self.num_items += 1
        self.array[self.tail] = x
        self.tail = (self.tail + 1) % len(self.array)
        return

    def dequeue(self) -> int:
        self.num_items -= 1
        res = self.array[self.head]
        self.head = (self.head + 1) % len(self.array)
        return res

    def size(self) -> int:
        return self.num_items


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
