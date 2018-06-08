"""
"""


def egg_dropping_puzzle():
    total = int(input())
    results = []
    for _ in range(total):
        egg, floor = [int(x) for x in input().split()]
        results.append(EggDroppingPuzzle(egg, floor).get_min_experiment_count())
    for i in results:
        print(i)


class EggDroppingPuzzle(object):

    def __init__(self, N, K):
        self.N = N
        self.K = K
        self.path = []
        self.cache_count = [[None for _ in range(K+1)] for __ in range(N+1)]
        self.cache_path = [[[None for _ in range(K+1)] for __ in range(K+1)] for ___ in range(N+1)]

    def get_min_experiment_count(self):
        result = self._get_min_experiment_count(self.N, self.K, 1, self.K)
        # result = self._get_min_experiment_path(self.N, self.K, 1, self.K, self.path)
        # print(self.path)
        return result

    def _get_min_experiment_count(self, N, K, start, end):
        if self.cache_count[N][K] is not None:
            return self.cache_count[N][K]
        if K == 0:
            self.cache_count[N][K] = 0
            return 0
        if K == 1:
            self.cache_count[N][K] = 1
            return 1
        if N == 1:
            self.cache_count[N][K] = K
            return K
        min_result = K + 1
        for i in range(start, end+1):
            result_break = self._get_min_experiment_count(N-1, i-start, start, i-1)
            result_safe = self._get_min_experiment_count(N, end-i, i+1, end)
            if result_break > result_safe and min_result > result_break:
                min_result = result_break
            elif result_break <= result_safe and min_result > result_safe:
                min_result = result_safe
        self.cache_count[N][K] = 1 + min_result
        return 1 + min_result

    def _get_min_experiment_path(self, N, K, start, end, path):
        if start < 1 or start > self.K or end < 1 or end > self.K  or start > end:
            return 0
        if self.cache_path[N][start][end] is not None:
            path.extend(self.cache_path[N][start][end][0])
            return self.cache_path[N][start][end][1]
        if K == 0:
            self.cache_path[N][start][end] = ([], 0)
            return 0
        if K == 1:
            path.append(start)
            self.cache_path[N][start][start] = (path, 1)
            return 1
        if N == 1:
            path.extend([x for x in range(start, end+1)])
            self.cache_path[N][start][end] = (path, K)
            return K
        min_result = K + 1
        for i in range(start, end+1):
            path_break = []
            path_safe = []
            result_break = self._get_min_experiment_path(N-1, i-start, start, i-1, path_break)
            result_safe = self._get_min_experiment_path(N, end-i, i+1, end, path_safe)
            if result_break > result_safe and min_result > result_break:
                min_result = result_break
                path.clear()
                path.append(i)
                path.extend(path_break)
            elif result_break <= result_safe and min_result > result_safe:
                min_result = result_safe
                path.clear()
                path.append(i)
                path.extend(path_safe)
        self.cache_path[N][start][end] = (path, 1 + min_result)
        return 1 + min_result

if __name__ == '__main__':
    egg_dropping_puzzle()
