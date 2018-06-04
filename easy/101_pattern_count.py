"""
"""


def pattern_101():
    total = int(input())
    results = []
    for _ in range(total):
        s = input()
        results.append(_pattern_101(s))
    for i in results:
        print(i)


def _pattern_101(s):
    result = 0
    first_1_index = -1
    has_zero = False
    length = len(s)
    for index in range(0, length):
        if s[index] == '1':
            if first_1_index == -1:
                first_1_index = index
            else:
                if has_zero:
                    first_1_index = index
                    has_zero = False
                    result += 1
                else:
                    first_1_index = index
        elif s[index] == '0':
            if first_1_index != -1:
                has_zero = True
        else:
            first_1_index = -1
            has_zero = False
    return result


if __name__ == "__main__":
    pattern_101()
