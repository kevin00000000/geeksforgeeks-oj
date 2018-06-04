"""
"""


def nth_fibonacci():
    total = int(input())
    results = []
    for _ in range(total):
        num = int(input())
        results.append(_get_nth_fibonacci(num) % 1000000007)
    for item in results:
        print(item)


def _get_nth_fibonacci(num):
    """
    bottom to top
    """
    if num == 1 or num == 2:
        return 1
    fib_array = []
    fib_array.append(1)
    fib_array.append(1)
    for i in range(2, num):
        fib_array.append(fib_array[i-2] + fib_array[i-1])
    return fib_array[num-1]


if __name__ == '__main__':
    nth_fibonacci()
