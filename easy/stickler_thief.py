"""
"""
from functools import reduce


def stickler_thief():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_stickler_thief(array, length))
    for i in results:
        print(i)


def _stickler_thief(array, length):
    if length <= 0:
        return 0
    elif length == 1:
        return array[0]
    elif length == 2:
        return max(array[0], array[1])
    result = [array[0], array[1]]
    max_prohit = max(array[0], array[1])
    for i in range(2, length):
        temp_profit = 0
        for j in range(i-1):
            if result[j] > temp_profit:
                temp_profit = result[j]
        result.append(temp_profit + array[i])
        if result[i] > max_prohit:
            max_prohit = result[i]
    return max_prohit


if __name__ == '__main__':
    stickler_thief()
