"""
"""


def edit_distance():
    total = int(input())
    results = []
    for _ in range(total):
        length1, length2 = [int(x) for x in input().split()]
        s1, s2 = input().split()
        results.append(EditDistanceTopDown(
            s1, length1, s2, length2).get_result())
    for i in results:
        print(i)


class EditDistanceTopDown(object):
    def __init__(self, s1, length1, s2, length2):
        self.s1 = s1
        self.s2 = s2
        self.length1 = length1
        self.length2 = length2
        self.cache = [[None for _ in range(length2+1)]
                      for __ in range(length1+1)]

    def get_result(self):
        return self._get_result(self.s1, self.length1, self.s2, self.length2)

    def _get_result(self, s1, length1, s2, length2):
        if self.cache[length1][length2] is not None:
            return self.cache[length1][length2]
        if length1 == 0 or length2 == 0:
            self.cache[length1][length2] = abs(length1-length2)
            return self.cache[length1][length2]
        if s1[length1-1] != s2[length2-1]:
            self.cache[length1][length2] = 1 + min(self._get_result(s1, length1, s2, length2-1), self._get_result(
                s1, length1-1, s2, length2), self._get_result(s1, length1-1, s2, length2-1))
        else:
            self.cache[length1][length2] = self._get_result(
                s1, length1-1, s2, length2-1)
        return self.cache[length1][length2]


if __name__ == '__main__':
    edit_distance()
