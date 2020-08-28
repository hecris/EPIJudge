from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    target = num_pairs * 2
    res = []
    def solution(s, balance):
        if balance < 0:
            return

        if balance + len(s) > target:
            return

        if len(s) == target:
            res.append(s)
            return

        solution(s+'(', balance + 1)
        solution(s+')', balance - 1)

    solution('', 0)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
