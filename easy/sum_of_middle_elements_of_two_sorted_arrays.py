"""
"""


def merged_array_mid_sum():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array1 = [int(x) for x in input().split()]
        array2 = [int(x) for x in input().split()]
        results.append(_merged_array_mid_sum(array1, array2, length))
    for i in results:
        print(i)


def _merged_array_mid_sum(array1, array2, length):
    result = []
    index_1 = 0
    index_2 = 0
    while index_1 < length and index_2 < length:
        if array1[index_1] < array2[index_2]:
            result.append(array1[index_1])
            index_1 += 1
        else:
            result.append(array2[index_2])
            index_2 += 1
    if index_1 < length:
        result.extend(array1[index_1:])
    else:
        result.extend(array2[index_2:])
    return result[length - 1] + result[length]


if __name__ == '__main__':
    merged_array_mid_sum()
