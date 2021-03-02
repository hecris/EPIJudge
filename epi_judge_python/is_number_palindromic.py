from test_framework import generic_test


def num_length(x):
    ans = 0
    while x:
        ans += 1
        x //= 10
    return ans

def is_palindrome_number(x: int) -> bool:
    if x <= 0: return x == 0
    n = num_length(x)
    msd_mask = 10 ** (n - 1)
    for _ in range(n//2):
        last_digit = x % 10
        first_digit = x // msd_mask
        if (first_digit != last_digit):
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
