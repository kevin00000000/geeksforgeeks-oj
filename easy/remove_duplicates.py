"""
"""


def remove_duplicate():
    total = int(input())
    results = []
    for _ in range(total):
        s = input()
        src = [c for c in s]
        results.append(_remove_duplicate(src))
    for r in results:
        print(r)


def _remove_duplicate(src):
    cache = [None for _ in range(256)]
    index_new = 0
    for index in range(len(src)):
        if cache[ord(src[index])] is None:
            cache[ord(src[index])] = 1
            src[index_new] = src[index]
            index_new += 1
    return ''.join(src[0:index_new])


if __name__ == '__main__':
    remove_duplicate()
