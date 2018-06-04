"""
"""
import math


def perfect_num():
    total = int(input())
    results = []
    for _ in range(total):
        num = int(input())
        results.append(_perfect_num(num))
    for i in results:
        print(i)


def _perfect_num(num):
    if num == 1:
        return 0
    max_factor = math.floor(math.sqrt(num))
    count = 1
    for i in range(2, max_factor+1):
        temp = num // i
        if temp == num / i:
            count += i
            if temp != i:
                count += num // i
    if count == num:
        return 1
    return 0


if __name__ == '__main__':
    perfect_num()
