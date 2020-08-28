import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from functools import lru_cache


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    @lru_cache(None)
    def solution(idx):
        if idx == len(domain): return True

        for i in range(idx+1, len(domain)+1):
            path.append(i)
            if domain[idx:i] in dictionary and solution(i):
                return True
            path.pop()

        return False

    path, res = [0], []
    solution(0)
    return [domain[path[i]:path[i+1]] for i in range(len(path) - 1)]


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
