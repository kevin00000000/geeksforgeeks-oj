"""
"""


def spiral_matrix():
    total = int(input())
    results = []
    for _ in range(total):
        array = []
        for _ in range(4):
            array.append([int(x) for x in input().split()])
        results.append(_spiral_matrix(array))
    for i in results:
        print(' '.join([str(x) for x in i]))


def _spiral_matrix(array):
    if len(array) == 0 or len(array[0]) == 0:
        return []
    high = len(array)
    width = len(array[0])
    left_top, right_top, left_bottom, right_bottom = (
        [0, 0], [0, width-1], [high-1, 0], [high-1, width-1])
    result = []
    while True:
        # left to right
        if left_top[1] <= right_top[1]:
            for i in range(left_top[1], right_top[1]+1):
                result.append(array[left_top[1]][i])
            left_top[0] += 1
            right_top[0] += 1
        else:
            break
        # top to bottom
        if right_top[0] <= right_bottom[0]:
            for i in range(right_top[0], right_bottom[0]+1):
                result.append(array[i][right_top[1]])
            right_top[1] -= 1
            right_bottom[1] -= 1
        else:
            break
        # right to left
        if left_bottom[1] <= right_bottom[1]:
            for i in range(right_bottom[1], left_bottom[1]-1, -1):
                result.append(array[left_bottom[0]][i])
            left_bottom[0] -= 1
            right_bottom[0] -= 1
        else:
            break
        # bottom to top
        if left_top[0] <= left_bottom[0]:
            for i in range(left_bottom[0], left_top[0]-1, -1):
                result.append(array[i][left_top[1]])
            left_top[1] += 1
            left_bottom[1] += 1
        else:
            break
    return result


if __name__ == '__main__':
    spiral_matrix()
