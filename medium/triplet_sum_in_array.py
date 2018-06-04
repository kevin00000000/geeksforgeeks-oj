"""
"""


def triplet_sum():
    total = int(input())
    results = []
    for _ in range(total):
        length, target = [int(x) for x in input().split()]
        array = [int(x) for x in input().split()]
        results.append(_triplet_sum(array, length, target))
    for i in results:
        print(i)


def _triplet_sum(array, length, target):
    for i in range(length):
        temp_target = target - array[i]
        if _two_sum(array, i+1, length-1, temp_target):
            return 1
    return 0


def _two_sum(array, start, end, target):
    cache = {}
    for i in range(start, end+1):
        if target-array[i] in cache:
            return True
        cache[array[i]] = None
    return False


if __name__ == '__main__':
    triplet_sum()
