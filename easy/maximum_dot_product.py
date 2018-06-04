"""
"""


def maximum_dot_product():
    total = int(input())
    results = []
    for _ in range(total):
        length1, length2 = [int(x) for x in input().split()]
        array1 = [int(x) for x in input().split()]
        array2 = [int(x) for x in input().split()]
        results.append(_maximum_dot_product(array1, array2, length1, length2))
    for i in results:
        print(i)


def _maximum_dot_product(array1, array2, length1, length2):
    maximum = [[None for __ in range(length2+1)] for _ in range(length1+1)]
    for l2 in range(length2+1):
        for l1 in range(length1+1):
            if l1 == 0 or l2 == 0:
                maximum[l1][l2] = 0
                continue
            if l1 < l2:
                maximum[l1][l2] = 0
                continue
            maximum[l1][l2] = max(maximum[l1-1][l2-1] +
                                  array1[l1-1]*array2[l2-1], maximum[l1-1][l2])
    return maximum[length1][length2]


if __name__ == '__main__':
    maximum_dot_product()
