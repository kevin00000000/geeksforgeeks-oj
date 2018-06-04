"""
"""


def max_tip():
    total = int(input())
    results = []
    for _ in range(total):
        N, X, Y = [int(x) for x in input().split()]
        array_x = [int(x) for x in input().split()]
        array_y = [int(x) for x in input().split()]
        results.append(_max_tip(N, X, Y, array_x, array_y))
    for i in results:
        print(i)


def _max_tip(N, X, Y, array_x, array_y):
    max_tip = 0
    cache = [[[None for _ in range(Y+1)] for __ in range(X+1)] for ___ in range(N+1)]
    cache[0][0][0] = 0
    for n in range(1, N+1):
        for x in range(X+1):
            if x > n:
                break
            for y in range(Y+1):
                if x + y > n:
                    break
                if x + y == n:
                    if x != 0 and y != 0:
                        cache[n][x][y] = max(cache[n-1][x][y-1] + array_y[n-1], cache[n-1][x-1][y] + array_x[n-1])
                    elif x == 0:
                        cache[n][x][y] = cache[n-1][x][y-1] + array_y[n-1]
                    else:
                        cache[n][x][y] = cache[n-1][x-1][y] + array_x[n-1]
                    if max_tip < cache[n][x][y]:
                        max_tip = cache[n][x][y]
    return max_tip


if __name__ == '__main__':
    max_tip()
