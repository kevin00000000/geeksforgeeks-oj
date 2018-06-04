"""
"""


def next_greater_set_digits():
    total = int(input())
    results = []
    for _ in range(total):
        n = int(input())
        results.append(_next_greater_set_digits(n))
    for i in results:
        if i == -1:
            print("not possible")
        else:
            print(i)


def _next_greater_set_digits(n):
    div_count = 0
    stack = []
    stack_temp = []
    while n != 0:
        digit = n % 10
        n = n // 10
        div_count += 1
        while len(stack) != 0 and stack[len(stack)-1] > digit:
            stack_temp.append(stack.pop())
        stack.append(digit)
        if len(stack_temp) != 0:
            n *= (10 ** div_count)
            div_count -= 1
            n += stack_temp.pop() * (10 ** div_count)
            while len(stack) != 0:
                stack_temp.append(stack.pop())
            while len(stack_temp) != 0:
                div_count -= 1
                n += stack_temp.pop() * (10 ** div_count)
            return n
    return -1


if __name__ == '__main__':
    next_greater_set_digits()
