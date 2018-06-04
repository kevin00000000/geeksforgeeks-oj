"""
"""


def anagram():
    total = int(input())
    results = []
    for _ in range(total):
        s1 = input()
        s2 = input()
        results.append(_anagram(s1, s2))
    for i in results:
        print(i)


def _anagram(s1, s2):
    cache1 = {}
    cache2 = {}
    for s in s1:
        try:
            cache1[s] += 1
        except KeyError:
            cache1[s] = 1
    for s in s2:
        try:
            cache2[s] += 1
        except KeyError:
            cache2[s] = 1
    if cache1 != cache2:
        return 'NO'
    return 'YES'
    # s_joint = s2 + s2
    # if s_joint.find(s1) == -1:
    #     return 'NO'
    # return 'YES'


if __name__ == '__main__':
    anagram()
