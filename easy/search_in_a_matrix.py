"""
"""


def sorted_matrix_search():
    total = int(input())
    results = []
    for _ in range(total):
        row, col = [int(x) for x in input().split()]
        array = [int(x) for x in input().split()]
        array = [[array[col*r + c] for c in range(col)] for r in range(row)]
        target = int(input())
        results.append(_sorted_matrix_search(row, col, array, target))
    for i in results:
        print(1) if i else print(0)


def _sorted_matrix_search(row, col, array, target):
    return _binary_search(0, 0, row-1, col-1, array, target)


def _binary_search(start_row, start_col, end_row, end_col, array, target):
    if start_row > end_row or start_col > end_col:
        return False
    mid_row = (start_row + end_row) // 2
    mid_col = (start_col + end_col) // 2
    if array[mid_row][mid_col] == target:
        return True
    elif array[mid_row][mid_col] > target:
        return (_binary_search(start_row, start_col, end_row-1, end_col-1, array, target) or _binary_search(mid_row, start_col, end_row, mid_col-1, array, target) or _binary_search(start_row, mid_col, end_row-1, end_col, array, target))
    else:
        return (_binary_search(mid_row+1, mid_col+1, end_row, end_col, array, target) or _binary_search(mid_row+1, start_col, end_row, mid_col, array, target) or _binary_search(start_row, mid_col+1, mid_row, end_col, array, target))


if __name__ == '__main__':
    sorted_matrix_search()
