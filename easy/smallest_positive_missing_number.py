"""
"""


def missing_smallest():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_missing_smallest(array, length))
    for i in results:
        print(i)


def _missing_smallest(array, length):
    result = 0
    cache = [None for _ in range(length)]
    for i in array:
        if i > 0 and i <= length:
            cache[i - 1] = 0
    for index, i in enumerate(cache):
        if i is None:
            result = index + 1
            break
    else:
        result = length + 1
    return result


if __name__ == '__main__':
    missing_smallest()
