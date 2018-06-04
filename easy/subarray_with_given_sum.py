"""
"""


def subarray_sum():
    total = int(input())
    results = []
    for _ in range(total):
        length, _sum = [int(x) for x in input().split()]
        array = [int(x) for x in input().split()]
        min_index = 0
        max_index = -1
        cur_sum = 0
        index = 0
        while index <= len(array):
            if cur_sum < _sum:
                if index < len(array):
                    max_index = index
                    cur_sum += array[index]
                index += 1
            elif cur_sum > _sum:
                cur_sum -= array[min_index]
                min_index += 1
            else:
                results.append((min_index+1, max_index+1))
                break
        else:
            results.append((-1, ))
    for r in results:
        print(' '.join([str(rr) for rr in r]))


if __name__ == '__main__':
    subarray_sum()