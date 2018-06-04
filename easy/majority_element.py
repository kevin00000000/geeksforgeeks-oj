"""
"""


def find_majority_element():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_find_majority_element(array, length))
    for i in results:
        print(i)


def _find_majority_element(array, length):
    cache = {}
    for i in array:
        try:
            cache[i] += 1
        except KeyError:
            cache[i] = 1
        if cache[i] > length//2:
            return i
    return 'NO Majority Element'


if __name__ == '__main__':
    find_majority_element()
