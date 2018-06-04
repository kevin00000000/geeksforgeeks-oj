"""
"""


def longest_distinct_substring():
    total = int(input())
    results = []
    for _ in range(total):
        s = input()
        results.append(_longest_distinct_substring(s))
    for i in results:
        print(i)


def _longest_distinct_substring(s):
    cache = {}
    start = 0
    cur_long = 0
    result = 0
    for index, c in enumerate(s):
        if c not in cache:
            cache[c] = index
            cur_long += 1
            if cur_long > result:
                result = cur_long
        else:
            temp = cache[c] + 1
            for i in range(start, cache[c]+1):
                cur_long -= 1
                del cache[s[i]]
            start = temp
            cache[c] = index
            cur_long += 1
    return result


if __name__ == '__main__':
    longest_distinct_substring()
