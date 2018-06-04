"""
"""


def first_non_repeating_char():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = input().split()
        results.append(_first_non_repeating_char(array, length))
    for i in results:
        print(' '.join([str(x) for x in i]))


def _first_non_repeating_char(array, length):
    char_count = {}
    char_order = []
    current_result_index = -1
    result = []
    for i in range(length):
        if array[i] not in char_count:
            char_count[array[i]] = 1
            char_order.append(array[i])
            if current_result_index == -1:
                current_result_index = len(char_order)-1
            result.append(char_order[current_result_index])
        else:
            char_count[array[i]] += 1
            if char_order[current_result_index] == array[i]:
                for j in range(current_result_index+1, len(char_order)):
                    if char_count[char_order[j]] == 1:
                        current_result_index = j
                        break
                else:
                    current_result_index = -1
            if current_result_index == -1:
                result.append(-1)
            else:
                result.append(char_order[current_result_index])
    return result


if __name__ == '__main__':
    first_non_repeating_char()
