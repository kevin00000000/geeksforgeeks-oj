"""
"""
import sys


def max_value():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_max_value(array, length))
    for i in results:
        print(i)


def _max_value(array, length):
    array_result = []
    for index in range(length):
        array_result.append(array[index] - index)
    min_value = sys.maxsize
    max_value = -sys.maxsize
    for i in array_result:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    return max_value-min_value


if __name__ == '__main__':
    max_value()
