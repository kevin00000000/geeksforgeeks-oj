"""
"""


def wave_array():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_wave_array(array, length))
    for l in results:
        print(' '.join([str(x) for x in l]))


def _wave_array(array, length):
    array = sorted(array)
    result = []
    i = 0
    while i < length:
        if i < length - 1:
            result.append(array[i+1])
            result.append(array[i])
            i += 2
        else:
            result.append(array[i])
            i += 1
    return result


if __name__ == '__main__':
    wave_array()
