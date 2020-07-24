from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    i, j = m - 1, n - 1
    write = m + n - 1

    while write >= 0:
        num1 = A[i] if i >= 0 else float('-inf')
        num2 = B[j] if j >= 0 else float('-inf')

        if num1 > num2:
            A[write] = num1
            i -= 1
        else:
            A[write] = num2
            j -= 1

        write -= 1

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
