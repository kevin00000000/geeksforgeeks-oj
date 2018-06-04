"""
"""


def small_int_sort():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_small_int_sort(array, length))
    for item in results:
        print(' '.join([str(x) for x in item]))


def _small_int_sort(array, length):
    array_count = [0, 0, 0]
    for i in array:
        array_count[i] += 1
    result = []
    for index, i in enumerate(array_count):
        result.extend([index]*i)
    return result


if __name__ == '__main__':
    small_int_sort()