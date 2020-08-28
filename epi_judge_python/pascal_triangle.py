from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n == 0:
        return []

    res = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = res[i-1]
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j+1])
        row.append(1)
        res.append(row)

    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
