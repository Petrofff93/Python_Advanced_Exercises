from collections import deque


def shooting_function(shooting_matrix, shooter_row, shooter_col, shooting_direction):
    target_coordinate = []
    while True:
        if shooting_direction == 'down':
            shooter_row += 1
            if 0 <= shooter_row < size and shooting_matrix[shooter_row][shooter_col] == 'x':
                target_coordinate = [shooter_row, shooter_col]
                shooting_matrix[shooter_row][shooter_col] = '.'
                return target_coordinate
            if shooter_row >= len(shooting_matrix):
                return

        elif shooting_direction == 'up':
            shooter_row -= 1
            if 0 <= shooter_row < size and shooting_matrix[shooter_row][shooter_col] == 'x':
                target_coordinate = [shooter_row, shooter_col]
                shooting_matrix[shooter_row][shooter_col] = '.'
                return target_coordinate
            if shooter_row < 0:
                return

        elif shooting_direction == 'left':
            shooter_col -= 1
            if 0 <= shooter_col < size and shooting_matrix[shooter_row][shooter_col] == 'x':
                target_coordinate = [shooter_row, shooter_col]
                shooting_matrix[shooter_row][shooter_col] = '.'
                return target_coordinate
            if shooter_col < 0:
                return

        elif shooting_direction == 'right':
            shooter_col += 1
            if 0 <= shooter_col < size and shooting_matrix[shooter_row][shooter_col] == 'x':
                target_coordinate = [shooter_row, shooter_col]
                shooting_matrix[shooter_row][shooter_col] = '.'
                return target_coordinate
            if shooter_col >= len(shooting_matrix):
                return


def moving_function(shooting_matrix, shooter_row, shooter_col, moving_direction, moving_steps):
    if moving_direction == 'left':
        col = shooter_col - moving_steps
        if 0 <= col < size and shooting_matrix[shooter_row][col] == '.':
            return shooter_row, col

    elif moving_direction == 'right':
        col = shooter_col + moving_steps
        if 0 <= col < size and shooting_matrix[shooter_row][col] == '.':
            return shooter_row, col

    elif moving_direction == 'up':
        row = shooter_row - moving_steps
        if 0 <= row < size and shooting_matrix[row][shooter_col] == '.':
            return row, shooter_col

    elif moving_direction == 'down':
        row = shooter_row + moving_steps
        if 0 <= row < size and shooting_matrix[row][shooter_col] == '.':
            return row, shooter_col


size = 5

shooting_matrix = []

targets = 0
shooter_row = 0
shooter_col = 0

for row in range(size):
    current_element = input().split()
    for col in range(size):
        if current_element[col] == 'A':
            shooter_row = row
            shooter_col = col
        elif current_element[col] == 'x':
            targets += 1
    shooting_matrix.append(current_element)


commands_count = int(input())
commands_q = deque()
targets_array = []
initial_targets = targets

for _ in range(commands_count):
    commands_q.append(input().split())

while commands_q and targets > 0:
    command = commands_q.popleft()

    if command[0] == 'shoot':
        shooting_direction = command[1]
        result = shooting_function(shooting_matrix, shooter_row, shooter_col, shooting_direction)
        if result:
            targets -= 1
            targets_array.append(result)

    if command[0] == 'move':
        moving_direction = command[1]
        moving_steps = int(command[2])
        result = moving_function(shooting_matrix, shooter_row, shooter_col, moving_direction, moving_steps)

        if result:
            shooting_matrix[shooter_row][shooter_col] = '.'
            shooter_row, shooter_col = result
            shooting_matrix[shooter_row][shooter_col] = 'A'

if targets > 0:
    print(f'Training not completed! {targets} targets left.')
    for element in targets_array:
        print(element)
else:
    print(f'Training completed! All {initial_targets} targets hit.')
    for element in targets_array:
        print(element)
