"""
"""


def reverse_word():
    total = int(input())
    results = []
    for _ in range(total):
        results.append('.'.join(input().split('.')[::-1]))
    for i in results:
        print(i)


if __name__ == '__main__':
    reverse_word()