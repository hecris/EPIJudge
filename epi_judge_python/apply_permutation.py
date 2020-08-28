from typing import List

from test_framework import generic_test


# NOTE: "The space complexity is O(n) since we modify the permutation array."
def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i in range(len(A)):
        if perm[i] == -1:
            continue
        else:
            replace = A[i]
            replace_pos = perm[i]
            while perm[replace_pos] != -1:
                replace, A[replace_pos] = A[replace_pos], replace
                perm[replace_pos], replace_pos = -1, perm[replace_pos]


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
