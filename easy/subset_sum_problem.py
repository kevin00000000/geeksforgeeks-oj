"""
"""
from functools import reduce
from copy import deepcopy


def subset_sum():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        _sum = reduce(lambda x, y: x + y, array)
        if _sum//2 == _sum/2:
            target = _sum // 2
        else:
            results.append('NO')
            continue
        # backtracking #
        result = []
        if _subset_sum_backtracking(array, target, 0, 0, result):
        # dynamic programming bottom_up
        # if _subset_sum_dynamicprogramming_bottom_up(array, length, target):
        # dynamic programming top_down
        # cache = [[None for i in range(target+1)] for j in range(length+1)]
        # if _subset_sum_dynamicprogramming_top_down(array, length, target, cache):
            results.append('YES')
        else:
            results.append('NO')
    for i in results:
        print(i)


def _subset_sum_backtracking(array, target, index, cur_sum, result):
    for sub_index, i in enumerate(array[index:]):
        if cur_sum + i == target:
            result.append(i)
            return True
        if cur_sum + i < target:
            result.append(i)
            b = _subset_sum_backtracking(
                array, target, index+1+sub_index, cur_sum+i, result)
            if b:
                return True
            else:
                result.pop()
    return False


def _subset_sum_dynamicprogramming_bottom_up(array, length, target):
    result = [[None for i in range(target+1)] for j in range(length+1)]
    for i in range(length+1):
        for j in range(target+1):
            if j == 0:
                result[i][j] = True
                continue
            if i == 0:
                result[i][j] = False
                continue
            if array[i-1] <= j:
                result[i][j] = result[i-1][j] or result[i-1][j-array[i-1]]
            else:
                result[i][j] = result[i-1][j]
    return result[length][target]


def _subset_sum_dynamicprogramming_top_down(array, n, target, cache):
    if n == 0:
        return False
    if target == 0:
        return True
    if cache[n][target] is not None:
        return cache[n][target]
    if array[n-1] > target:
        cache[n][target] = _subset_sum_dynamicprogramming_top_down(
            array, n-1, target, cache)
    else:
        cache[n][target] = _subset_sum_dynamicprogramming_top_down(
            array, n-1, target, cache) or _subset_sum_dynamicprogramming_top_down(array, n-1, target-array[n-1], cache)
    return cache[n][target]


def get_all_combine(array, length):
    result = []
    if length == 0:
        return [[]]
    sub_result = get_all_combine(array[1:], length-1)
    result.extend(sub_result)
    sub_result = deepcopy(sub_result)
    [item.append(array[0]) for item in sub_result]
    result.extend(sub_result)
    return result


if __name__ == '__main__':
    subset_sum()
