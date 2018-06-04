"""
"""


def max_out_of_three_element():
    total = int(input())
    results = []
    for _ in range(total):
        length, k = [int(x) for x in input().split()]
        array = [int(x) for x in input().split()]
        results.append(_max_out_of_three_element(array, length, k))
    for i in results:
        print(' '.join([str(x) for x in i]))


def _max_out_of_three_element(array, length, k):
    if length < k:
        return []
    result = []
    max_index = -1
    max_temp = 0
    for i in range(0, length-k+1):
        if i <= max_index:
            if array[i+k-1] > max_temp:
                max_temp = array[i+k-1]
                max_index = i+k-1
        else:
            max_temp = 0
            for j in range(i, i+k):
                if array[j] > max_temp:
                    max_temp = array[j]
                    max_index = j
        result.append(max_temp)
    return result


if __name__ == '__main__':
    max_out_of_three_element()
