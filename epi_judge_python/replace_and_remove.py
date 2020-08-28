import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# NOTE: Was close, but had to get hint from solution
def replace_and_remove(size: int, s: List[str]) -> int:
    write = 0
    resize = 0
    for i in range(size):
        if s[i] != 'b':
            s[write] = s[i]
            write += 1
        if s[i] == 'a':
            resize += 1

    read, write = write, write + resize - 1
    res = write + 1
    for i in reversed(range(read)):
        if s[i] == 'a':
            s[write] = 'd'
            s[write-1] = 'd'
            write -= 2
        else:
            s[write] = s[i]
            write -= 1

    return res


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
