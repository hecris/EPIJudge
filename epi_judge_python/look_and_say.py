from test_framework import generic_test


# NOTE: Could use char array instead of string
def look_and_say(n: int) -> str:
    def next_number(s):
        i = 0
        res = ''
        while i < len(s):
            count = 1
            while i < len(s) - 1 and s[i] == s[i+1]:
                count += 1
                i += 1
            res += str(count) + s[i]
            i += 1
        return res

    res = '1'
    for i in range(1, n):
        res = next_number(res)

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
