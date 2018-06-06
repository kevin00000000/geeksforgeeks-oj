"""
"""


def coin_change():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        M = int(input())
        results.append(_coin_change(array, length, M))
    for i in results:
        print(i)


def _coin_change(array, N, M):
    result = [[None for _ in range(N+1)] for __ in range(M+1)]
    for m in range(M+1):
        for n in range(N+1):
            if m == 0:
                result[m][n] = 1
                continue
            if n == 0:
                result[m][n] = 0
                continue
            if array[n-1] > m:
                result[m][n] = result[m][n-1]
            else:
                result[m][n] = result[m][n-1]
                i = 1
                while m >= i * array[n-1]:
                    result[m][n] += result[m-array[n-1]*i][n-1]
                    i += 1
    return result[M][N]


if __name__ == '__main__':
    coin_change()
