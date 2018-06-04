"""
"""
import functools


def longest_increasing_subarray():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_longest_increasing_subarray(array, length))
    for i in results:
        print(i)


def _longest_increasing_subarray(array, length):
    max_length = 0
    max_length_array = [0 for _ in range(length)]
    for i in range(length):
        if i == 0:
            max_length_array[i] = 1
        else:
            max_length_array[i] = max([max_length_array[x]+1 for x in range(i) if array[i] > array[x]], default=1)
        if max_length_array[i] > max_length:
            max_length = max_length_array[i]
    return max_length


if __name__ == '__main__':
    longest_increasing_subarray()
