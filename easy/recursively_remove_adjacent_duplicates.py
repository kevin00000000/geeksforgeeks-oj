"""
"""


def remove_adjacent_duplicate():
    total = int(input())
    results = []
    for _ in range(total):
        s = input()
        results.append(_remove_adjacent_duplicate(s))
    for s in results:
        print(s)


def _remove_adjacent_duplicate(s):
    s_new = _remove(s)
    if s_new == s:
        return s
    return _remove_adjacent_duplicate(s_new)


def _remove(s):
    stack = []
    last_c = ''
    count = 1
    for c in s:
        if c == last_c:
            stack.append(c)
            count += 1
        else:
            if count > 1:
                # clear
                for _ in range(count):
                    stack.pop()
                count = 1
            last_c = c
            stack.append(c)
    if count > 1:
        # clear
        for _ in range(count):
            stack.pop()
    return ''.join(stack)


if __name__ == '__main__':
    remove_adjacent_duplicate()
