"""
"""
import sys
import math


def sum_closer_zero():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_sum_closer_zero(array, length))
    for item in results:
        print(' '.join([str(x) for x in item]))


def _sum_closer_zero(array, length):
    min_abs = sys.maxsize
    result = [-1, -1]
    array = sorted(array)
    l = 0
    r = length - 1
    while l != r:
        temp = array[l] + array[r]
        temp_abs = abs(temp)
        if temp_abs < min_abs:
            min_abs = temp_abs
            result[0] = array[l]
            result[1] = array[r]
        if temp > 0:
            r -= 1
        elif temp < 0:
            l += 1
        else:
            return result
    return result


if __name__ == '__main__':
    sum_closer_zero()
