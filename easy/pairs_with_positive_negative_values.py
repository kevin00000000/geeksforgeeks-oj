"""
"""


def two_sum_zero():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_two_sum_zero(array))
    for item in results:
        if len(item) == 0:
            print(0)
        else:
            print(' '.join([' '.join([str(y) for y in x]) for x in item]))


def _two_sum_zero(array):
    cache = {}
    result = []
    for i in array:
        if -i in cache:
            if i < -i:
                result.append((i, -i))
            else:
                result.append((-i, i))
        else:
            cache[i] = None
    return sorted(result, key=lambda elem: elem[1])


if __name__ == '__main__':
    two_sum_zero()
