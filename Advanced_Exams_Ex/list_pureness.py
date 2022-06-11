from collections import deque


def best_list_pureness(*args):
    rotations = args[-1]
    pure_list = deque(args[0])
    pure_dict = {}

    for rotation in range(rotations + 1):

        current_sum = 0
        for idx, num in enumerate(pure_list):
            current_sum += num * idx
        pure_dict[rotation] = current_sum
        pure_list.appendleft(pure_list.pop())

    key = (max(pure_dict, key=lambda x: pure_dict[x]))
    return f'Best pureness {pure_dict[key]} after {key} rotations'

