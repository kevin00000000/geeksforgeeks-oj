"""
"""


def longest_parlindrome_substring():
    total = int(input())
    results = []
    for _ in range(total):
        s = input()
        results.append(_longest_parlindrome_substring(s))
    for i in results:
        print(i)


def _longest_parlindrome_substring(s):
    length = len(s)
    if length == 0:
        return ''
    max_length = 0
    max_length_low = 0
    max_length_high = 0
    cache = [[None for _ in range(length)] for __ in range(length)]
    for high in range(length):
        for low in range(length-1, -1, -1):
            if low >= high:
                cache[low][high] = True
            else:
                cache[low][high] = cache[low+1][high-1] and s[low] == s[high]
            if cache[low][high]:
                if max_length < high-low+1:
                    max_length = high-low+1
                    max_length_high = high
                    max_length_low = low
    return s[max_length_low:max_length_high+1]


if __name__ == '__main__':
    longest_parlindrome_substring()
