"""
"""
import sys
from collections import deque


def left_smaller_right_larger():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_left_smaller_right_larger(array, length))
    for i in results:
        print(i)


def _left_smaller_right_larger(array, length):
    max_left = deque([-sys.maxsize])
    min_right = deque([sys.maxsize])
    result = None
    for i in range(1, length):
        max_left.append(max(max_left[i-1], array[i-1]))
    for i in range(length-2, -1, -1):
        min_right.appendleft(min(min_right[0], array[i+1]))
    for i in range(1, length-1):
        if max_left[i] <= array[i] <= min_right[i]:
            result = array[i]
            break
    else:
        result = -1
    return result


if __name__ == '__main__':
    left_smaller_right_larger()
