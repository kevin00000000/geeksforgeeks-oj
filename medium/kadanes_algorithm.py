"""
"""
import sys


def max_sum_subarray():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_max_sum_array(array, length))
    for i in results:
        print(i)


def _max_sum_array(array, length):
    max_sum = -sys.maxsize
    max_sum_array = [0 for _ in range(length)]
    last_max_sum = 0
    for i in range(length):
        if i > 0:
            last_max_sum = max_sum_array[i-1]
        max_sum_cur = last_max_sum + array[i]
        if max_sum_cur > max_sum:
            max_sum = max_sum_cur
        max_sum_array[i] = max_sum_cur if max_sum_cur > 0 else 0
    return max_sum


if __name__ == '__main__':
    max_sum_subarray()
