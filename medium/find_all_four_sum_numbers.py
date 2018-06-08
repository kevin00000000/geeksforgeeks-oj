"""
"""


def find_all_four_sum_numbers():
    total = int(input())
    results = []
    for _ in range(total):
        length, K = [int(x) for x in input().split()]
        array = [int(x) for x in input().split()]
        results.append(FindAllFourSumNumbers(array, length, K, 4).get_all())
    for list_a in results:
        if len(list_a) == 0:
            print(-1)
        else:
            tuple_b = []
            for item in list_a:
                tuple_b.append(tuple(item))
            set_c = set(tuple_b)
            list_a = sorted(list(set_c))
            for item in list_a:
                print(' '.join([str(x) for x in item]), end=' $')
            print('')


class FindAllFourSumNumbers(object):

    def __init__(self, array, length, K, target_length):
        self.array = sorted(array)
        self.length = length
        self.K = K
        self.target_length = target_length
        self.result = []

    def get_all(self):
        self.result.clear()
        self._get_all(0, self.K, self.target_length, [])
        return self.result

    def _get_all(self, start, K, target_length, cache):
        if target_length <= 0 or start >= self.length:
            return
        if target_length > 1:
            for i in range(start, self.length-(target_length-1)):
                cache.append(self.array[i])
                self._get_all(i+1, K-self.array[i], target_length-1, cache)
                cache.pop()
        if target_length == 1:
            for i in range(start, self.length):
                if self.array[i] == K:
                    temp = cache.copy()
                    temp.append(self.array[i])
                    self.result.append(temp)
                elif self.array[i] > K:
                    return


if __name__ == '__main__':
    find_all_four_sum_numbers()
