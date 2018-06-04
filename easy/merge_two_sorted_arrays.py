"""
"""


def merge_array():
    total = int(input())
    results = []
    for _ in range(total):
        length1, length2 = [int(x) for x in input().split()]
        array1 = [int(x) for x in input().split()]
        array2 = [int(x) for x in input().split()]
        results.append(_merge_array(array1, length1, array2, length2))
    for r in results:
        print(" ".join([str(x) for x in r]))


def _merge_array(array1, length1, array2, length2):
    result = []
    l1 = 0
    l2 = 0
    while l1 < length1 and l2 < length2:
        if array1[l1] < array2[l2]:
            result.append(array1[l1])
            l1 += 1
        else:
            result.append(array2[l2])
            l2 += 1
    if l1 == length1:
        result.extend(array2[l2:])
    else:
        result.extend(array1[l1:])
    return result[::-1]


if __name__ == '__main__':
    merge_array()
