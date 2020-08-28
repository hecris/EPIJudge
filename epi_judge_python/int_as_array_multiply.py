from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    res = [0]
    for i in reversed(range(len(num1))):
        write = len(num1) - i - 1
        for j in reversed(range(len(num2))):
            if write + 1 > len(res):
                res.append(0)
            res[write] += num1[i] * num2[j]
            write += 1

    carry = 0
    for i in range(len(res)):
        res[i] += carry
        carry = res[i] // 10
        res[i] %= 10

    if carry > 0:
        res.append(carry)

    res.reverse()
    res[0] *= sign

    start = next((i for i,x in enumerate(res) if x != 0), len(res))
    return res[start:] or [0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
