from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    if not path:
        return path

    l = path.split('/')

    stack = []
    for item in l:
        if not item or item == '.':
            continue

        if item == '..' and stack and stack[-1] != '..':
                stack.pop()
        else:
            stack.append(item)

    return ('/' if path[0] == '/' else '') + '/'.join(stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
