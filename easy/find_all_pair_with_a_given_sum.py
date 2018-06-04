"""
"""


def all_pair_given_sum():
    total = int(input())
    results = []
    for _ in range(total):
        len1, len2, _sum = [int(x) for x in input().split()]
        array1 = [int(x) for x in input().split()]
        array2 = [int(x) for x in input().split()]
        results.append(_all_pair_giver_sum(array1, array2, len1, len2, _sum))
    for index_tuple_list in results:
        if len(index_tuple_list) == 0:
            print(-1)
        else:
            print(', '.join([' '.join([str(x) for x in t])
                            for t in index_tuple_list]))


def _all_pair_giver_sum(array1, array2, len1, len2, _sum):
    array1_map = {}
    result = []
    for i in array2:
        array1_map[i] = None
    for j in array1:
        if (_sum - j) in array1_map:
            result.append((j, _sum-j))
    return sorted(result, key=lambda x: x[0])


if __name__ == '__main__':
    all_pair_given_sum()
