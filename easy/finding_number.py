"""
"""


def finding_element():
    total = int(input())
    results = []
    for _ in range(total):
        length, target = [int(x) for x in input().split()]
        array = [int(x) for x in input().split()]
        results.append(_finding_element(array, length, target))
    for i in results:
        if i == -1:
            print('OOPS! NOT FOUND')
        else:
            print(i)


def _finding_element(array, length, target):
    largest_index = -1
    if length == 1:
        largest_index = 0
    else:
        largest_index = _find_largest(array, 0, length-1)
    result = _find_element_in_increasing(array, 0, largest_index, "I", target)
    if result == -1:
        return _find_element_in_increasing(array, largest_index, length-1, 'D', target)
    return result


def _find_largest(array, start, end):
    if start > end:
        raise ValueError('Empty array')
    mid = (start+end) // 2
    if mid != start and mid != end:
        if array[mid-1] <= array[mid] >= array[mid+1]:
            return mid
        elif array[mid-1] > array[mid] > array[mid+1]:
            return _find_largest(array, start, mid-1)
        else:
            return _find_largest(array, mid+1, end)
    elif mid == start:
        return start
    else:
        return end



def _find_element_in_increasing(array, start, end, sequeue_type, target):
    if start > end:
        return -1
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif (sequeue_type == 'I' and array[mid] > target) or (sequeue_type == 'D' and array[mid] < target):
        return _find_element_in_increasing(array, start, mid-1, sequeue_type, target)
    else:
        return _find_element_in_increasing(array, mid+1, end, sequeue_type, target)


if __name__ == '__main__':
    finding_element()
