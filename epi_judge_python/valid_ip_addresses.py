from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    def is_valid(s):
        return len(s) > 0 and (len(s) == 1 or (s[0] != '0' and int(s) <= 255))

    res = []
    address = []
    for i in range(min(3, len(s))):
        if not is_valid(s[:i+1]):
            continue
        address.append(s[:i+1])
        for j in range(i+1, min(i+4, len(s))):
            if not is_valid(s[i+1:j+1]):
                continue
            address.append(s[i+1:j+1])
            for k in range(j+1, min(j+4, len(s))):
                if not is_valid(s[j+1:k+1]):
                    continue
                if not is_valid(s[k+1:]):
                    continue
                address.append(s[j+1:k+1])
                address.append(s[k+1:])
                res.append('.'.join(address))
                address.pop()
                address.pop()

            address.pop()

        address.pop()

    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
