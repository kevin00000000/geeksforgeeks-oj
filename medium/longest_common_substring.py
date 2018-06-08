"""
"""


def longest_common_substring():
    total = int(input())
    results = []
    for _ in range(total):
        length1, length2 = [int(x) for x in input().split()]
        s1 = input()
        s2 = input()
        results.append(_longest_common_substring(s1, length1, s2, length2))
    for i in results:
        print(i)


def _longest_common_substring(s1, length1, s2, length2):
    longest_common_substring = 0
    cache = [[0 for _ in range(length2)] for __ in range(length1)]
    for i in range(length1):
        for j in range(length2):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    cache[i][j] = 1
                else:
                    cache[i][j] = cache[i-1][j-1] + 1
            if cache[i][j] > longest_common_substring:
                longest_common_substring = cache[i][j]
    return longest_common_substring


if __name__ == '__main__':
    longest_common_substring()
