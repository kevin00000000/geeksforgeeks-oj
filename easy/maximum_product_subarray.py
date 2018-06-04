"""
"""


def maximum_product_subarray():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_maximum_product_subarray(array, length))
    for i in results:
        print(i)


def _maximum_product_subarray(array, lenght):
    max_product = 1
    max_product_array = []
    min_product_array = []
    for l in range(0, lenght):
        if array[l] == 0:
            max_product_array.append(1)
            min_product_array.append(1)
            continue
        if l == 0:
            max_product_array.append(array[0] if array[0] >= 1 else 1)
            min_product_array.append(array[0] if array[0] <= -1 else 1)
            max_product = max_product_array[0]
            continue
        if array[l] > 0:
            max_temp = max_product_array[l - 1] * array[l]
            min_temp = min_product_array[l - 1] * array[l]
            max_product_array.append(max_temp if max_temp >= 1 else 1)
            min_product_array.append(min_temp if min_temp <= -1 else 1)
            if max_temp > max_product:
                max_product = max_temp
        else:
            max_temp = min_product_array[l - 1] * array[l]
            min_temp = max_product_array[l - 1] * array[l]
            max_product_array.append(max_temp if max_temp >= 1 else 1)
            min_product_array.append(min_temp if min_temp <= -1 else 1)
            if max_temp > max_product:
                max_product = max_temp
    return max_product


if __name__ == '__main__':
    maximum_product_subarray()
