"""
"""


def inversion_count():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_inversion_count(array, length))
    for i in results:
        print(i)


def _inversion_count(array, length):
    stack_master = []
    stack_slave = []
    result = 0
    for i in array:
        while len(stack_master) != 0 and stack_master[len(stack_master)-1] > i:
            result += 1
            stack_slave.append(stack_master.pop())
        stack_master.append(i)
        while len(stack_slave) != 0:
            stack_master.append(stack_slave.pop())
    return result


if __name__ == '__main__':
    inversion_count()
