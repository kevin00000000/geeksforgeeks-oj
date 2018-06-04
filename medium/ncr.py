"""
"""


def n_c_r():
    total = int(input())
    results = []
    for _ in range(total):
        n, r = [int(x) for x in input().split()]
        results.append(NCR(n, r).n_c_r())
    for i in results:
        print(i % (10**9+7))


class NCR(object):
    def __init__(self, n, r):
        self.n = n
        self.r = r
        self.cache = [[None for _ in range(r+1)] for __ in range(n+1)]

    def n_c_r(self):
        return self._n_c_r_bottom_up(self.n, self.r)

    def _n_c_r(self, n, r):
        if r > n:
            return 0
        if self.cache[n][r] is not None:
            return self.cache[n][r]
        if r == 0:
            self.cache[n][r] = 1
        else:
            self.cache[n][r] = self._n_c_r(n-1, r) + self._n_c_r(n-1, r-1)
        return self.cache[n][r]

    def _n_c_r_bottom_up(self, n, r):
        cache = [[None for _ in range(r+1)] for __ in range(n+1)]
        for i in range(n+1):
            for j in range(r+1):
                if j > i:
                    cache[i][j] = 0
                    continue
                if j == 0:
                    cache[i][j] = 1
                else:
                    cache[i][j] = cache[i-1][j] + cache[i-1][j-1]
        return cache[n][r]


if __name__ == '__main__':
    n_c_r()
