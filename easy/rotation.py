"""
"""


def rotated_count():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_rotated_count(array, length))
    for _ in results:
        print(_)


def _rotated_count(array, length):
    if length <= 1:
        return 0
    for i in range(1, length):
        if array[i-1] > array[i]:
            return i
    return 0


if __name__ == '__main__':
    rotated_count()
