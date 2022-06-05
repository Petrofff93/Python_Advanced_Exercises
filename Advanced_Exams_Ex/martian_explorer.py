from collections import deque


def get_position(rover_row, rover_col, current_command):
    if current_command == 'up':
        return rover_row - 1, rover_col
    elif current_command == 'down':
        return rover_row + 1, rover_col
    elif current_command == 'left':
        return rover_row, rover_col - 1
    elif current_command == 'right':
        return rover_row, rover_col + 1


def is_inside(new_rol, new_col, size):
    return 0 <= new_rol < size and 0 <= new_col < size


size = 6
matrix = []

rover_row = 0
rover_col = 0

concrete = 0
water = 0
metal = 0

for row in range(size):
    current_element = input().split()
    for col in range(size):
        if current_element[col] == 'E':
            rover_row = row
            rover_col = col
    matrix.append(current_element)

commands_q = deque(x for x in input().split(', '))

while commands_q:
    current_command = commands_q.popleft()
    new_row, new_col = get_position(rover_row, rover_col, current_command)

    if is_inside(new_row, new_col, size):
        rover_row, rover_col = new_row, new_col
    else:
        if new_row >= size:
            rover_row = 0
            rover_col = new_col

        if new_row < 0:
            rover_row = 5
            rover_col = new_col

        if new_col >= size:
            rover_row = new_row
            rover_col = 0

        if new_col < 0:
            rover_row = new_row
            rover_col = 5

    if matrix[rover_row][rover_col] == 'W':
        print(f"Water deposit found at ({rover_row}, {rover_col})")
        water += 1
    elif matrix[rover_row][rover_col] == 'M':
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
        metal += 1
    elif matrix[rover_row][rover_col] == 'C':
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
        concrete += 1
    elif matrix[rover_row][rover_col] == 'R':
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if water > 0 and concrete > 0 and metal > 0:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')






