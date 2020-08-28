from test_framework import generic_test


def evaluate(expression: str) -> int:
    l = expression.split(',')
    ops = {'+': lambda x,y: x+y, '-': lambda x,y: x-y, '*': lambda x,y: x*y, '/': lambda x,y: x//y}
    stack = []
    for item in l:
        if item in ops:
            y,x = stack.pop(), stack.pop()
            stack.append(ops[item](x,y))
            pass
        else:
            stack.append(int(item))

    return stack[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
