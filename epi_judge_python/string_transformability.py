from typing import Set

from test_framework import generic_test
from collections import deque


def transform_string(D: Set[str], s: str, t: str) -> int:
    q = deque([s])
    distance = 0
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node == t:
                return distance

            if node not in D:
                continue

            D.remove(node)

            for i in range(len(node)):
                for c in range(26):
                    char = chr(ord('a') + c)
                    tmp = node[:i] + char + node[i+1:]
                    if tmp in D:
                        q.append(tmp)

        distance += 1

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
