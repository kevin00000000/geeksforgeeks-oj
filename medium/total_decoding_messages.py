"""
"""


def total_decoding():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        s = input()
        results.append(TotalDecoding(s, length).get_total_message())
    for i in results:
        print(i)


class TotalDecoding(object):

    def __init__(self, s, length):
        self.array = [int(x) for x in s]
        self.length = length
        self.cache = [None for _ in range(length+1)]

    def get_total_message(self):
        return self._get_total_message(self.length)

    def _get_total_message(self, l):
        if l < 0:
            return 0
        if l == 0:
            return 1
        if self.cache[l] is not None:
            return self.cache[l]
        if self.array[self.length-l] == 0:
            self.cache[l] = 0
        elif self.array[self.length-l] == 1:
            self.cache[l] = self._get_total_message(
                l-1) + self._get_total_message(l-2)
        elif self.array[self.length-l] == 2:
            if l > 1 and self.array[self.length-l+1] <= 6:
                self.cache[l] = self._get_total_message(
                    l-1) + self._get_total_message(l-2)
            else:
                self.cache[l] = self._get_total_message(l-1)
        else:
            self.cache[l] = self._get_total_message(l-1)
        return self.cache[l]


if __name__ == '__main__':
    total_decoding()
