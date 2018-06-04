"""
"""


def permutation():
    total = int(input())
    results = []
    for _ in range(total):
        array = [x for x in input()]
        results.append(_permutation(array, 0, len(array)-1))
    for item in results:
        for j in sorted(item):
            print(''.join([str(x) for x in j]), end=' ')
        print('')


def _permutation(array, start, end):
    result = []
    if start > end:
        return [[]]
    for i in range(start, end+1):
        array[start], array[i] = array[i], array[start]
        for item in _permutation(array, start+1, end):
            temp_list = [array[start]]
            temp_list.extend(item)
            result.append(temp_list)
        array[i], array[start] = array[start], array[i]
    return result


if __name__ == '__main__':
    permutation()
