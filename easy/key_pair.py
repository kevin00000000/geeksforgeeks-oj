"""
"""


def two_sum():
    total = int(input())
    results = []
    for _ in range(total):
        length, _sum = [int(x) for x in input().split()]
        array = [int(x) for x in input().split()]
        cache = {}
        for i in array:
            if (_sum - i) in cache:
                results.append('YES')
                break
            else:
                cache[i] = None
        else:
            results.append('NO')
    for i in results:
        print(i)


if __name__ == '__main__':
    two_sum()