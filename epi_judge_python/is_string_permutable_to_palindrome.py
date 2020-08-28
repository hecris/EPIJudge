from test_framework import generic_test
from collections import Counter


def can_form_palindrome(s: str) -> bool:
    return len([x for x in Counter(s).values() if x % 2]) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
