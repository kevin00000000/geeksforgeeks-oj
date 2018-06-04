"""
"""


def word_boggle():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array_s = input().split()
        length_n, length_m = [int(x) for x in input().split()]
        temp = [x for x in input().split()]
        array_matrix = [[temp[length_m*j+i]
                         for i in range(length_m)] for j in range(length_n)]
        result = set()
        for i in array_s:
            if WordBoggle(i, array_matrix, length_n, length_m).is_valid():
                result.add(i)
        results.append(result)
    for i in results:
        if len(i) == 0:
            print(-1)
        else:
            print(' '.join(sorted(i)))


class WordBoggle(object):

    def __init__(self, s, array_matrix, length_n, length_m):
        self.s = s
        self.length = len(s)
        self.array_matrix = array_matrix
        self.length_n = length_n
        self.length_m = length_m
        self.mark = [[True for _ in range(length_m)] for __ in range(length_n)]

    def is_valid(self):
        if self.length == 0:
            return True
        for n in range(self.length_n):
            for m in range(self.length_m):
                if self.array_matrix[n][m] == self.s[0] and self._is_valid(1, n, m):
                    return True
        return False

    def _is_valid(self, index, n, m):
        if index == self.length:
            return True
        self.mark[n][m] = False
        for i in range(n-1, n+2):
            for j in range(m-1, m+2):
                if 0 <= i < self.length_n and 0 <= j < self.length_m:
                    if self.s[index] == self.array_matrix[i][j] and self.mark[i][j]:
                        if not self._is_valid(index+1, i, j):
                            self.mark[i][j] = True
                        else:
                            return True
        return False


if __name__ == '__main__':
    word_boggle()
