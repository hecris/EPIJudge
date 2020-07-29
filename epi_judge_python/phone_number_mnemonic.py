from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    LETTERS = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

    def solution(lo):
        if lo == len(phone_number):
            return ['']

        recurse = solution(lo+1)
        res = []

        for letter in LETTERS[int(phone_number[lo])]:
            for word in recurse:
                res.append(letter + word)

        return res

    return solution(0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
