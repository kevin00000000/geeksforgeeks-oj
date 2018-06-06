"""
"""


class BinaryHeap(object):

    def __init__(self):
        self.array = [None]
        self.length = 0

    def max(self):
        if self.length:
            return self.array[1]

    def replace_max(self, item):
        if self.length == 0:
            return
        self.array.append(item)
        self.length += 1
        self.delete_max()
        return

    def insert(self, item):
        self.array.append(item)
        self.length += 1
        index = self.length
        while index//2 > 0:
            if self.array[index] > self.array[index//2]:
                self.array[index], self.array[index//2] = self.array[index//2], self.array[index]
                index //= 2
            else:
                break

    def delete_max(self):
        if self.length == 0:
            return None
        max_value = self.max()
        self.array[1] = self.array[self.length]
        self.length -= 1
        self.array.pop()
        self._sink()
        return max_value

    def _sink(self):
        index = 1
        while index*2 <= self.length:
            if index*2+1 <= self.length:
                if self.array[index] < max(self.array[index*2], self.array[index*2+1]):
                    if self.array[index*2] > self.array[index*2+1]:
                        self.array[index], self.array[index*2] = self.array[index*2], self.array[index]
                        index *= 2
                    else:
                        self.array[index], self.array[index*2+1] = self.array[index*2+1], self.array[index]
                        index = index * 2 + 1
                else:
                    break
            else:
                if self.array[index] < self.array[index*2]:
                    self.array[index], self.array[index*2] = self.array[index*2], self.array[index]
                    index *= 2
                else:
                    break
        return


def kth_smallest_element():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        K = int(input())
        results.append(_kth_smallest_element(array, length, K))
    for i in results:
        print(i)


def _kth_smallest_element(array, length, K):
    binary_heap = BinaryHeap()
    for i in range(K):
        binary_heap.insert(array[i])
    for i in range(K, length):
        if array[i] < binary_heap.max():
            binary_heap.replace_max(array[i])
    return binary_heap.max()


if __name__ == '__main__':
    kth_smallest_element()
