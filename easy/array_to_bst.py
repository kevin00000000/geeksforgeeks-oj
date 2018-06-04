"""
"""


class Node(object):
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value


def sorted_array_to_bbst():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_sorted_array_to_bbst(array, 0, length - 1))
    for root in results:
        result = []
        get_preorder(root, result)
        print(" ".join([str(x) for x in result]))


def _sorted_array_to_bbst(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    left_node = _sorted_array_to_bbst(array, start, mid - 1)
    right_node = _sorted_array_to_bbst(array, mid + 1, end)
    node = Node(left_node, right_node, array[mid])
    return node


def get_preorder(root, result):
    if root is not None:
        result.append(root.value)
        get_preorder(root.left, result)
        get_preorder(root.right, result)


if __name__ == '__main__':
    sorted_array_to_bbst()
