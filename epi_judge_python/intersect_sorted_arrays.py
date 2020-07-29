from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    # NOTE: cool Python one-liner to get distinct elements
    # and demonstration of bisect
    # import bisect
    # def search(arr, target):
    #     k = bisect.bisect_left(arr, target)
    #     return k < len(arr) and arr[k] == target

    # return [a for i, a in enumerate(A) if (i == 0 or A[i-1] != a) and search(B, a)]
    res = []
    i = j = 0
    while True:
        # go to next distinct value in A
        while i < len(A) - 1 and A[i] == A[i+1]:
            i += 1

        # go to next distinct value in B
        while j < len(B) - 1 and B[j] == B[j+1]:
            j += 1

        if i >= len(A) or j >= len(B):
            break

        if A[i] == B[j]:
            res.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
