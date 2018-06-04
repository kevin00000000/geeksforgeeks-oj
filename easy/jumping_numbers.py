"""
"""
from math import log10, floor


def jumping_number():
    total = int(input())
    results = []
    for _ in range(total):
        num = int(input())
        results.append(_jumping_number(num))
    for i in results:
        print(' '.join([str(x) for x in i]))


def _jumping_number(num):
    if num == 0:
        return [0]
    result = []
    digit = 0
    copy_num = num
    top_digit_num = 0
    while copy_num != 0:
        digit += 1
        top_digit_num = copy_num % 10
        copy_num //= 10
    for i in range(1, digit+1):
        if i == 1:
            result.extend([x for x in range(0, 10)])
        elif 1 < i < digit:
            for j in range(1, 10):
                result.extend(_get_jumping_number_list(i, j))
        else:
            for j in range(1, top_digit_num+1):
                result.extend(_get_jumping_number_list(digit, j))
    return sorted([i for i in result if i <= num], key=lambda x: 0 if x == 0 else x // (10**floor(log10(x))))


def _get_jumping_number_list(digit, num):
    result = []
    if digit == 1:
        return [num]
    if num == 0:
        result.extend(_get_jumping_number_list(digit-1, 1))
    elif num == 9:
        result.extend(_get_jumping_number_list(digit-1, 8))
    else:
        result.extend(_get_jumping_number_list(digit-1, num-1))
        result.extend(_get_jumping_number_list(digit-1, num+1))
    return [num*10**(digit-1)+i for i in result]


if __name__ == '__main__':
    jumping_number()
