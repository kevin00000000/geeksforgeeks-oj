"""
"""
import sys
from collections import deque

def larger_element():
    total = int(input())
    results = []
    for _ in range(total):
        length = int(input())
        array = [int(x) for x in input().split()]
        results.append(_larger_element(array))
    for item in results:
        print(' '.join([str(x) for x in item]))


def _larger_element(array):
    stack = deque([])
    result = []
    last_push = sys.maxsize
    for index, value in enumerate(array):
        result.append(None)
        if value <= last_push:
            stack.append((index, value))
            last_push = value
        else:
            while len(stack):
                pop_index, pop_value = stack.pop()
                if pop_value < value:
                    result[pop_index] = value
                else:
                    stack.append((pop_index, pop_value))
                    stack.append((index, value))
                    last_push = value
                    break
            else:
                stack.append((index, value))
                last_push = value
    while len(stack):
        pop_index, pop_value = stack.pop()
        result[pop_index] = -1
    return result


# def _larger_element(array):
#     state = []
#     result = []
#     up_or_down = None
#     diff = [array[index+1]-value for index, value in enumerate(array[0:len(array)-1])]
    
#     for index, i in enumerate(diff):
#         if index == 0:
#             if i > 0:
#                 up_or_down = True
#                 state.append({'start_end':[0, None], 'state':up_or_down})
#             else:
#                 up_or_down = False
#                 state.append({'start_end':[0, None], 'state':up_or_down})
#         else:
#             if not ((i>0 and up_or_down is True) or (i<=0 and up_or_down is False)):
#                 state[len(state)-1]["start_end"][1] = index - 1
#                 up_or_down = False if up_or_down else True
#                 state.append({'start_end':[index, None], 'state':up_or_down})
#     state[len(state)-1]["start_end"][1] = len(array)-1
#     for index, x in enumerate(array):
#         for s in state:
#             if index >= s["start_end"][0] and index <= s["start_end"][1]:
#                 if s['state']:
#                     result.append(array[index+1] if index+1<len(array) else -1)
#                 else:
#                     for ii, ss in enumerate(state):
#                         if index < ss["start_end"][0] and ss["state"] and x < array[min(ss["start_end"][1]+1, len(array)-1)]:
#                             for xx in array[ss['start_end'][0]:min(ss['start_end'][1]+1+1, len(array))]:
#                                 if xx > x:
#                                     result.append(xx)
#                             break
#                     else:
#                         result.append(-1)
#                 break
#     return result


if __name__ == '__main__':
    larger_element()