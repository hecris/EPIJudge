from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    d = {
        ')': '(',
        '}': '{',
        ']': '[',
            }

    stack = []

    for char in s:
        if char in d:
            if not stack:
                return False

            if stack[-1] == d[char]:
                stack.pop()
            else:
                return False
        else:
            # open
            stack.append(char)

    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
