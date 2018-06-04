"""
"""


def star_super_star():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_star_super_star(array, length))
    for super_star, star in results:
        print(' '.join([str(x) for x in star]))
        print(super_star)


def _star_super_star(array, length):
    left_max = 0
    right_max = 0
    left_max_array = [0 for _ in range(length)]
    right_max_array = [0 for _ in range(length)]
    for index in range(1, length):
        if array[index-1] > left_max:
            left_max = array[index-1]
        left_max_array[index] = left_max
    for index in range(length-2, -1, -1):
        if array[index+1] > right_max:
            right_max = array[index+1]
        right_max_array[index] = right_max
    super_star = -1
    star = []
    for index, value in enumerate(array):
        if value > left_max_array[index] and value > right_max_array[index]:
            super_star = value
            star.append(value)
        elif value > right_max_array[index]:
            star.append(value)
        else:
            pass
    return super_star, star



if __name__ == '__main__':
    star_super_star()
