"""
"""


def once_in_sorted_array():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_once_in_sorted_array(array, length))
    for i in results:
        print(i)


def _once_in_sorted_array(array, length):
    result = None
    for i in array:
        if result:
            result ^= i
        else:
            result = i
    return result


if __name__ == '__main__':
    once_in_sorted_array()
