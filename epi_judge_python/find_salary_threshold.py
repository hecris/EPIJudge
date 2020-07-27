from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()
    n = len(current_salaries)
    pre = [0]
    for i in range(1, n):
        pre.append(pre[i-1] + current_salaries[i-1])

    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi) >> 1
        remain = n - mid
        payroll = pre[mid] + current_salaries[mid] * remain
        if payroll < target_payroll:
            lo = mid + 1
        else:
            hi = mid

    ans = (target_payroll - pre[hi]) / (n - hi)
    return -1 if ans > current_salaries[-1] else ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
