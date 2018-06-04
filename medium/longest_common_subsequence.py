"""
"""


def longest_common_subsequeue():
    total = int(input())
    results = []
    for _ in range(total):
        length1, length2 = [int(x) for x in input().split()]
        array1 = input()
        array2 = input()
        results.append(_longest_common_subsequeue(
            array1, array2, length1, length2))
    for i in results:
        print(i)


def _longest_common_subsequeue(array1, array2, length1, length2):
    max_length = 0
    max_length_array = [[None for _ in range(
        length2+1)] for __ in range(length1+1)]
    for i in range(length1+1):
        for j in range(length2+1):
            if i == 0 or j == 0:
                max_length_array[i][j] = 0
            else:
                if array1[i-1] == array2[j-1]:
                    max_length_array[i][j] = max_length_array[i-1][j-1] + 1
                else:
                    max_length_array[i][j] = max(
                        max_length_array[i-1][j], max_length_array[i][j-1])
            if max_length_array[i][j] > max_length:
                max_length = max_length_array[i][j]
    return max_length


if __name__ == '__main__':
    longest_common_subsequeue()
