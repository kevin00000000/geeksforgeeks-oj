"""
"""


def trapping_rain_water():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_trapping_rain_water(array, length))
    for i in results:
        print(i)


def _trapping_rain_water(array, length):
    if length < 3:
        return 0
    stack = _get_all_maximum_large_point(array, length)
    stack = _clear_stack(array, stack)
    return _get_total_rain_water(array, stack)


def _get_all_maximum_large_point(array, length):
    stack = []
    find_large = True
    for i in range(length):
        if find_large:
            if i < length - 1 and array[i] > array[i+1]:
                stack.append(i)
                find_large = not find_large
        else:
            if i < length - 1 and array[i] < array[i+1]:
                find_large = not find_large
    if find_large:
        stack.append(length-1)
    return stack


def _clear_stack(array, stack):
    stack_status = []
    stack_temp = []
    while len(stack):
        v = stack.pop()
        if len(stack_temp) == 0:
            stack_temp.append(v)
            stack_status.append(False)
            continue
        if array[v] > array[stack_temp[len(stack_temp)-1]]:
            if stack_status[len(stack_status)-1]:
                stack_temp.pop()
                stack_status.pop()
                stack.append(v)
            else:
                stack_temp.append(v)
                stack_status.append(False)
        else:
            stack_temp.append(v)
            stack_status.append(True)
    return stack_temp[::-1]


def _get_total_rain_water(array, stack):
    if len(stack) < 2:
        return 0
    result = 0
    for i in range(1, len(stack)):
        standard = min(array[stack[i-1]], array[stack[i]])
        for v in range(stack[i-1]+1, stack[i]):
            diff = standard - array[v]
            if diff > 0:
                result += diff
    return result


if __name__ == '__main__':
    trapping_rain_water()
