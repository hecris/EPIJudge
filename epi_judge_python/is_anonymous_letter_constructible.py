from test_framework import generic_test
from collections import Counter


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    c = Counter(magazine_text)
    for char in letter_text:
        if c[char] == 0:
            return False
        c[char] -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
