from test_framework import generic_test


def power(x: float, y: int) -> float:
    if y < 0:
        x = 1 / x
        y *= -1

    # iterative
    ans = 1
    while y:
        if y & 1:
            ans *= x
        x *= x
        y >>= 1

    return ans

    # recursive
    def solution(x,y):
        if (y == 0): return 1
        if (y == 1): return x
        recurse = solution(x, y//2)
        return recurse * recurse * (x if y % 2 else 1)

    return solution(x,y)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
