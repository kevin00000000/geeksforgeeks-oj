"""
"""
from functools import reduce


def equilibrium_point():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        base_left = 0
        base_right = 0
        results.append(_equilibrium_point(array, 0, length-1, base_left, base_right))
    for i in results:
        print(i)


def _equilibrium_point(array, start, end, base_left, base_right):
    if start > end:
        return -1
    mid = (start + end) // 2
    current_left = reduce(lambda x, y: x + y, array[start:mid], 0)
    current_right = reduce(lambda x, y: x + y, array[mid+1:end+1], 0)
    sum_left = base_left + current_left
    sum_right = base_right + current_right
    if sum_left > sum_right:
        base_right += current_right+array[mid]
        return _equilibrium_point(array, start, mid-1, base_left, base_right)
    elif sum_left < sum_right:
        base_left += current_left+array[mid]
        return _equilibrium_point(array, mid+1, end, base_left, base_right)
    else:
        return mid+1


if __name__ == '__main__':
    equilibrium_point()