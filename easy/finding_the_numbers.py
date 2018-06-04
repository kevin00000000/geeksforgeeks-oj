"""
"""


def finding_the_nums():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_finding_the_num(array, length))
    for item in results:
        print(' '.join([str(x) for x in item]))


def _finding_the_num(array, length):
    cache = {}
    result = []
    for i in array:
        try:
            cache[i] += 1
        except:
            cache[i] = 1
        if cache[i] == 2:
            del cache[i]
    result = [x for x in cache.keys()]
    return sorted(result)


if __name__ == '__main__':
    finding_the_nums()
