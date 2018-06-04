"""
"""


def pythagorean_triplet():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_pythagorean_triplet(array, length))
    for i in results:
        print(i)


def _pythagorean_triplet(array, length):
    cache_square = {i: i*i for i in array}
    cache = {}
    for i in array:
        cache.clear()
        for j in array:
            if j < i:
                if (cache_square[i]-cache_square[j]) in cache:
                    return 'Yes'
                else:
                    cache[cache_square[j]] = None
    return 'No'


if __name__ == '__main__':
    pythagorean_triplet()
