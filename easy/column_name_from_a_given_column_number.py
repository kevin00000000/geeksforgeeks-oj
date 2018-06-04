"""
"""


def digit_to_excel_column():
    total = int(input())
    results = []
    for _ in range(total):
        n = int(input())
        results.append(_digit_to_excel_column(n))
    for i in results:
        print(i)


def _digit_to_excel_column(n):
    dictionary = {}
    result = []
    for i in range(1, 27):
        dictionary[i] = chr(ord('A') + i -1)
    dictionary[0] = 'Z'
    while n != 0:
        result.append(dictionary[n % 26])
        if n % 26 == 0:
            n -= 1
        n = n // 26
    return ''.join(result[::-1])


if __name__ == '__main__':
    digit_to_excel_column()
