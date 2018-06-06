"""
"""


def is_binary_number_multiple_of_3():
    total = int(input())
    results = []
    for _ in range(total):
        s = input()
        results.append(_is_binary_number_multiple_of_3(s))
    for i in results:
        print(i)


def _is_binary_number_multiple_of_3(s):
    rule = [{} for _ in range(3)]
    rule[0]['0'] = 0
    rule[0]['1'] = 1
    rule[1]['0'] = 2
    rule[1]['1'] = 0
    rule[2]['0'] = 1
    rule[2]['1'] = 2
    status = 0
    for i in s:
        status = rule[status][i]
    if status == 0:
        return 1
    return 0


if __name__ == '__main__':
    is_binary_number_multiple_of_3()
