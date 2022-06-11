def snake_direction(direction, snake_row, snake_col):
    if direction == 'right':
        return snake_row, snake_col + 1
    elif direction == 'left':
        return snake_row, snake_col - 1
    elif direction == 'up':
        return snake_row - 1, snake_col
    elif direction == 'down':
        return snake_row + 1, snake_col


def is_valid_direction(matrix, current_row, current_col):
    return 0 <= current_row < len(matrix) and 0 <= current_col < len(matrix)


size = int(input())
matrix = []

snake_row, snake_col = 0, 0
burrow1_row, burrow1_col = 0, 0
burrow2_row, burrow2_col = 0, 0

food_quantity = 0

burrow_found = False
for row in range(size):
    current_element = [x for x in input()]
    for col in range(size):
        if current_element[col] == 'B' and not burrow_found:
            burrow1_row = row
            burrow1_col = col
            burrow_found = True
        elif current_element[col] == 'B' and burrow_found:
            burrow2_row = row
            burrow2_col = col
        elif current_element[col] == 'S':
            snake_row = row
            snake_col = col
    matrix.append(current_element)

while True:
    if food_quantity == 10:
        break
    direction = input()
    current_row, current_col = snake_direction(direction, snake_row, snake_col)

    if not is_valid_direction(matrix, current_row, current_col):
        matrix[snake_row][snake_col] = '.'
        break

    matrix[snake_row][snake_col] = '.'
    snake_row, snake_col = current_row, current_col

    if matrix[snake_row][snake_col] == '*':
        food_quantity += 1
        matrix[snake_row][snake_col] = 'S'

    elif matrix[snake_row][snake_col] == 'B':
        if snake_row == burrow1_row and snake_col == burrow1_col:
            snake_row, snake_col = burrow2_row, burrow2_col
            matrix[snake_row][snake_col] = 'S'
            matrix[burrow1_row][burrow1_col] = '.'
        else:
            snake_row, snake_col = burrow2_row, burrow2_col
            matrix[snake_row][snake_col] = 'S'
            matrix[burrow2_row][burrow2_col] = '.'

    matrix[snake_row][snake_col] = 'S'

if food_quantity >= 10:
    print('You won! You fed the snake.')
    print(f'Food eaten: {food_quantity}')

    for element in matrix:
        print(''.join(element))
else:
    print('Game over!')
    print(f'Food eaten: {food_quantity}')
    for element in matrix:
        print(''.join(element))
