"""
"""


def get_max_profit():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_get_max_profit(array, length))
    for i in results:
        if len(i) == 0:
            print('No Profit')
        else:
            print(' '.join(['('+' '.join([str(y) for y in x])+')' for x in i]))


def _get_max_profit(array, length):
    result = []
    minima = -1
    maxima = -1
    while maxima != length - 1:
        for j in range(maxima + 1, length):
            if j < length-1 and array[j] < array[j+1]:
                minima = j
                break
        else:
            return result
        for k in range(j, length):
            if k < length - 1 and array[k] > array[k+1]:
                maxima = k
                break
        else:
            maxima = length - 1
        result.append((minima, maxima))
    return result


if __name__ == '__main__':
    get_max_profit()
