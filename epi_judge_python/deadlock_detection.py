import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from collections import defaultdict


class GraphVertex:
    def __init__(self) -> None:
        self.edges: List['GraphVertex'] = []


def is_deadlocked(graph: List[GraphVertex]) -> bool:
    # WHITE, GRAY, BLACK
    TO_PROCESS, SEEN, PROCESSED = range(3)
    status = defaultdict(int)
    def dfs(node):
        if status[node] == SEEN:
            return True

        status[node] = SEEN
        if any(dfs(adj) for adj in node.edges):
            return True

        status[node] = PROCESSED
        return False

    return any(status[node] == TO_PROCESS and dfs(node) for node in graph)


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('deadlock_detection.py',
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
