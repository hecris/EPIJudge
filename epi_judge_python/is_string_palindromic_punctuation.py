from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    lo, hi = 0, len(s) - 1
    while True:
        while lo < len(s) and not s[lo].isalnum():
            lo += 1

        while hi >= 0 and not s[hi].isalnum():
            hi -= 1

        if lo >= hi:
            break

        if s[lo].lower() != s[hi].lower():
            return False

        lo += 1
        hi -= 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
