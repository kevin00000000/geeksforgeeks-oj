"""
"""
from collections import deque


def max_sum_increasing_sequeue():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_max_sum_increasing_sequeue(array, length))
    for i in results:
        print(i)


def _max_sum_increasing_sequeue(array, length):
    result = array[:]
    max_sum = array[0]
    for i in range(1, length):
        for j in range(i):
            if array[i] > array[j] and array[i] + result[j] > result[i]:
                result[i] = array[i] + result[j]
        max_sum = max(result[i], max_sum)
    return max_sum


if __name__ == '__main__':
    max_sum_increasing_sequeue()
