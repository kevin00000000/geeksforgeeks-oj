"""
"""


def power_2():
    total_count = int(input())
    results = []
    for _ in range(total_count):
        num = int(input())
        if num == 0:
            results.append('NO')
            continue
        while num != 0:
            if num & 0b1:
                num >>= 1
                if num == 0:
                    results.append('YES')
                else:
                    results.append('NO')
                break
            num >>= 1
    for i in results:
        print(i)


if __name__ == '__main__':
    power_2()
