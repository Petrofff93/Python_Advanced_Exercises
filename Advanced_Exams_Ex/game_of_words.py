from collections import deque


def get_player_pos(player_row, player_col, direction):
    if direction == 'up':
        return player_row - 1, player_col
    elif direction == 'down':
        return player_row + 1, player_col
    elif direction == 'left':
        return player_row, player_col - 1
    elif direction == 'right':
        return player_row, player_col + 1


def is_valid_movement(new_row, new_col, size):
    return 0 <= new_row < size and 0 <= new_col < size


initial_string = [x for x in input()]
size = int(input())

matrix = []
commands = deque()
player_row = 0
player_col = 0

for row in range(size):
    current_element = [x for x in input()]
    for col in range(len(current_element)):
        if current_element[col] == 'P':
            player_row = row
            player_col = col
    matrix.append(current_element)

commands_count = int(input())

for _ in range(commands_count):
    commands.append(input())

while commands:
    direction = commands.popleft()
    new_row, new_col = get_player_pos(player_row, player_col, direction)

    if is_valid_movement(new_row, new_col, size):
        matrix[player_row][player_col] = '-'
        player_row, player_col = new_row, new_col

        if matrix[player_row][player_col] != '-':
            initial_string.append(matrix[player_row][player_col])
        matrix[player_row][player_col] = 'P'
    else:
        if initial_string:
            initial_string.pop()


print(''.join(initial_string))

for el in matrix:
    print(''.join(el))




