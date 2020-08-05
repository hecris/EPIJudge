from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    ans = []
    placement = [0] * n
    rows = set()
    diag1 = set()
    diag2 = set()

    def solution(row):
        if row == n:
            ans.append(placement.copy())
            return

        for choice in range(n):
            if choice in rows:
                continue

            d1 = row - choice
            d2 = row + choice
            if d1 in diag1 or d2 in diag2:
                continue

            rows.add(choice)
            diag1.add(d1)
            diag2.add(d2)
            placement[row] = choice

            solution(row+1)

            rows.remove(choice)
            diag1.remove(d1)
            diag2.remove(d2)


    solution(0)
    return ans


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
