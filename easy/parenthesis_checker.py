"""
"""


def check_balanced():
    total = int(input())
    results = []
    for _ in range(total):
        seq = input()
        results.append(_check_balanced(seq))
    for i in results:
        print(i)


def _check_balanced(seq):
    stack = []
    for c in seq:
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
        elif c == '}' or c == ']' or c == ')':
            if len(stack) == 0:
                return 'not balanced'
            pop_c = stack.pop()
            if not ((c == '}' and pop_c == '{') or (c == ']' and pop_c == '[') or (c == ')' and pop_c == '(')):
                return 'not balanced'
        else:
            pass
    if len(stack) != 0:
        return 'not balanced'
    return 'balanced'


if __name__ == '__main__':
    check_balanced()
