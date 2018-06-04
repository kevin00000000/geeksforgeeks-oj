"""
"""
from collections import deque


def minimum_num_jupm():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_minimum_num_jupm(array, length))
    for i in results:
        print(i)


def _minimum_num_jupm(array, length):
    marked = [False for _ in range(length)]
    level = [0 for _ in range(length)]
    q = deque([])
    q.append(0)
    level[0] = 0
    marked[0] = True
    while(len(q)):
        index = q.popleft()
        if index == length - 1:
            return level[index]
        if array[index] == 0:
            continue
        for i in range(1, array[index]+1):
            next_step = index + i
            if next_step == length-1:
                return level[index] + 1
            if not marked[next_step]:
                marked[next_step] = True
                level[next_step] = level[index] + 1
                q.append(next_step)
    return -1


if __name__ == '__main__':
    minimum_num_jupm()
