"""
"""

def k_largest():
    total = int(input())
    results = []
    for _ in range(total):
        length, k = [int(x) for x in input().split()]
        array = [int(x) for x in input().split()]
        results.append(get_k_largest(array, length, k))
    for item in results:
        print(' '.join([str(x) for x in item]))


def get_k_largest(array, length, k):
    binary_heap = [None]
    current_length = 0
    for index, value in enumerate(array):
        binary_heap.append(value)
        current_length += 1
        index += 1
        while index != 1:
            if binary_heap[index] > binary_heap[index//2]:
                binary_heap[index], binary_heap[index//2] = binary_heap[index//2], binary_heap[index]
                index //= 2
            else:
                break
    result = []
    for i in range(k):
        result.append(binary_heap[1])
        binary_heap[1] = binary_heap[current_length]
        current_length -= 1
        index = 1
        while index * 2 <= current_length:
            if index*2+1 <= current_length:
                if binary_heap[index*2] > binary_heap[index*2+1]:
                    if binary_heap[index] < binary_heap[index*2]:
                        binary_heap[index], binary_heap[index*2] = binary_heap[index*2], binary_heap[index]
                        index *= 2
                    else:
                        break
                else:
                    if binary_heap[index] < binary_heap[index*2+1]:
                        binary_heap[index], binary_heap[index*2+1] = binary_heap[index*2+1], binary_heap[index]
                        index = index*2 + 1
                    else:
                        break
            else:
                if binary_heap[index] < binary_heap[index*2]:
                    binary_heap[index], binary_heap[index*2] = binary_heap[index*2], binary_heap[index]
                    index *= 2
                else:
                    break
    return result


if __name__ == '__main__':
    k_largest()
