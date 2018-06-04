"""
"""
import sys


def make_change_coin():
    total = int(input())
    results = []
    for _ in range(total):
        target, length = [int(x) for x in input().split()]
        array = [int(x) for x in input().split()]
        # results.append(_make_change_coin(array, length, target))
        _init_cache_(target)
        results.append(_make_change_coin_top_down(array, length, target))
        # results.append(_make_change_coin_bottom_up(array, length, target))
    for i in results:
        if i == sys.maxsize:
            print(-1)
        else:
            print(i)


def _make_change_coin(array, length, target):
    if target == 0:
        return 0
    min_num = sys.maxsize
    for i in array:
        if i <= target:
            temp_sum = _make_change_coin(array, length, target - i)
            if temp_sum != sys.maxsize and temp_sum + 1 < min_num:
                min_num = temp_sum + 1
    return min_num


cache_top_down = []


def _init_cache_(target):
    global cache_top_down
    cache_top_down = [None for _ in range(target+1)]
    cache_top_down[0] = 0


def _make_change_coin_top_down(array, length, target):
    global cache_top_down
    if cache_top_down[target] is None:
        min_num = sys.maxsize
        for i in array:
            if i <= target:
                temp_sum = _make_change_coin_top_down(
                    array, length, target - i)
                if temp_sum != sys.maxsize and temp_sum + 1 < min_num:
                    min_num = temp_sum + 1
        cache_top_down[target] = min_num
    return cache_top_down[target]


def _make_change_coin_bottom_up(array, length, target):
    cache_bottom_up = [None for _ in range(target+1)]
    cache_bottom_up[0] = 0
    for i in range(1, target+1):
        min_num = sys.maxsize
        for j in array:
            if j <= i:
                temp_num = cache_bottom_up[i - j] + 1
                if temp_num < min_num:
                    min_num = temp_num
        cache_bottom_up[i] = min_num
    return cache_bottom_up[target]


if __name__ == '__main__':
    make_change_coin()
