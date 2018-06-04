"""
"""


def get_smallest_element():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_get_small_element(array, 0, length-1, length))
    for _ in results:
        print(_)


def _get_small_element(array, start, end, length):
    if start > end:
        return None
    if length == 1:
        return array[0]
    mid = (start + end) // 2
    if _is_smallest(array, mid, length):
        return array[mid]
    if _is_sorted(array, mid, end):
        return _get_small_element(array, start, mid-1, length)
    else:
        return _get_small_element(array, mid+1, end, length)


def _is_sorted(array, start, end):
    if array[start] < array[end]:
        return True
    else:
        return False


def _is_smallest(array, index, length):
    if 0 < index < length-1:
        return array[index-1] > array[index] and array[index] < array[index+1]
    elif index == 0:
        return array[index] < array[index + 1]
    else:
        return array[index] < array[index - 1]


if __name__ == '__main__':
    get_smallest_element()
