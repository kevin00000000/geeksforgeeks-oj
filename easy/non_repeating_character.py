"""
"""
from functools import reduce


def non_repeated():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        s = input()
        results.append(_non_repeated(s, length))
    for i in results:
        print(i)


def _non_repeated(s, length):
    cache = {}
    cache_index = {}
    for index, value in enumerate(s):
        try:
            cache[value] += 1
        except:
            cache[value] = 1
            cache_index[value] = index
    cache = {key: value for key, value in cache.items() if value == 1}
    result = -1
    min_index = length
    for key in cache.keys():
        if cache_index[key] < min_index:
            result = key
            min_index = cache_index[key]
    return result


if __name__ == '__main__':
    non_repeated()
