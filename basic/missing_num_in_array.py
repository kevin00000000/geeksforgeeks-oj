"""
"""


"""
"""


def missing_num_unsorted():
    total_count = int(input())
    results = []
    for _ in range(total_count):
        length = int(input())
        array = [int(x) for x in input().split()]
        result = _missing_num_unsorted(array, length)
        results.append(result)
    for i in results:
        print(i)


def _missing_num_unsorted(array, length):
    cache = {}
    for i in array:
        cache[i] = 1
    for i in range(1, length+1):
        if i not in cache:
            return i
    return 0


if __name__ == '__main__':
    missing_num_unsorted()
