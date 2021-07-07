from typing import List

from test_framework import generic_test
import math
import bintrees


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    RAD2 = math.sqrt(2)
    res = []
    tree = bintrees.RBTree()
    tree.insert((0, 0, 0), 0)
    while k > 0:
        x = tree.pop_min()[0]
        val, a, b = x
        res.append(val)

        next1 = a + 1 + b * RAD2
        next2 = a + (b + 1) * RAD2

        tree.insert((next1, a+1, b), 0)
        tree.insert((next2, a, b+1), 0)
        k -= 1

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
