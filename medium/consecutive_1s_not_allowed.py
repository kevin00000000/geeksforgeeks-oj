"""
"""
from math import factorial


def no_consecutive_1():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        results.append(_no_consecutive_1(length))
    for i in results:
        print(i % (10**9+7))


def _no_consecutive_1(length):
    total_1 = 0
    total_num = 0
    while total_1 <= length-total_1+1:
        total_num += factorial(length-total_1+1) // (factorial(length+1-total_1-total_1) * factorial(total_1))
        total_1 += 1
    return total_num


if __name__ == '__main__':
    no_consecutive_1()
