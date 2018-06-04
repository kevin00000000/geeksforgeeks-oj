"""
"""


def find_element():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        target = int(input())
        results.append(_find_element(array, 0, length-1, target))
    for i in results:
        print(i)


def _find_element(array, start, end, target):
    if start > end:
        return -1
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    if _is_sorted(array, start, mid-1):
        if _is_in_sorted_range(array, start, mid-1, target):
            return _find_element(array, start, mid-1, target)
        else:
            return _find_element(array, mid+1, end, target)
    else:
        if _is_in_sorted_range(array, mid+1, end, target):
            return _find_element(array, mid+1, end, target)
        else:
            return _find_element(array, start, mid-1, target)


def _is_sorted(array, start, end):
    if start > end:
        return False
    elif start < end:
        return array[start] < array[end]
    else:
        return True


def _is_in_sorted_range(array, start, end, target):
    if start > end:
        return False
    return array[start] <= target <= array[end]


if __name__ == '__main__':
    find_element()
