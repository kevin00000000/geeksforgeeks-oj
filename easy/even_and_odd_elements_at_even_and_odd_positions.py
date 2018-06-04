"""
"""


def odd_even_index():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_odd_even_index(array, length))
    for i in results:
        print(' '.join([str(x) for x in i]))


def _odd_even_index(array, length):
    result = []
    array_odd = []
    array_even = []
    for i in array:
        if i % 2 == 0:
            array_even.append(i)
        else:
            array_odd.append(i)
    len_odd = len(array_odd)
    len_even = len(array_even)
    index_odd = 0
    index_even = 0
    index = 0
    while index_odd < len_odd and index_even < len_even:
        if index % 2 == 0:
            result.append(array_even[index_even])
            index_even += 1
        else:
            result.append(array_odd[index_odd])
            index_odd += 1
        index += 1
    if index_odd < len_odd:
        result.extend(array_odd[index_odd:])
    else:
        result.extend(array_even[index_even:])
    return result


if __name__ == '__main__':
    odd_even_index()
