"""
"""


def contain_123():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_contain_123(array, length))
    for l in results:
        if len(l):
            print(' '.join([str(x) for x in l]))
        else:
            print(-1)


def _contain_123(array, length):
    result = []
    for i in array:
        if _validate_123(i):
            result.append(i)
    return sorted(result)


def _validate_123(num):
    if num == 0:
        return False
    while num:
        digit = num % 10
        num //= 10
        if not (1 <= digit <= 3):
            return False
    return True


if __name__ == '__main__':
    contain_123()
