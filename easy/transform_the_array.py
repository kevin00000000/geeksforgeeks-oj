"""
"""


def transform_array():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_transform_array(array, length))
    for i in results:
        print(' '.join([str(x) for x in i]))


def _transform_array(array, length):
    stack_valid = []
    stack_invalid = []
    for i in array:
        if i == 0:
            stack_invalid.append(i)
        else:
            this_one = i
            # while len(stack_valid):
            if len(stack_valid):
                last_one = stack_valid.pop()
                if last_one == this_one:
                    stack_invalid.append(0)
                    this_one *= 2
                else:
                    stack_valid.append(last_one)
                    # break
            stack_valid.append(this_one)
    stack_valid.extend(stack_invalid)
    return stack_valid


if __name__ == '__main__':
    transform_array()
