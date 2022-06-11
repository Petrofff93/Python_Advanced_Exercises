def calculate_position(row, col, matrix):
    counter = 0

    # calculate left
    if 0 <= col - 1 < len(matrix):
        if matrix[row][col - 1] == '*':
            counter += 1

    # calculate right
    if 0 <= col + 1 < len(matrix):
        if matrix[row][col + 1] == '*':
            counter += 1

    # calculate up
    if 0 <= row - 1 < len(matrix):
        if matrix[row - 1][col] == '*':
            counter += 1

    # calculate down
    if 0 <= row + 1 < len(matrix):
        if matrix[row + 1][col] == '*':
            counter += 1

    # calculate upper left diagonal
    if 0 <= row - 1 < len(matrix) and 0 <= col - 1 < len(matrix):
        if matrix[row - 1][col - 1] == '*':
            counter += 1

    # calculate upper right diagonal
    if 0 <= row - 1 < len(matrix) and 0 <= col + 1 < len(matrix):
        if matrix[row - 1][col + 1] == '*':
            counter += 1

    # calculate bottom left diagonal
    if 0 <= row + 1 < len(matrix) and 0 <= col - 1 < len(matrix):
        if matrix[row + 1][col - 1] == '*':
            counter += 1

    # calculate bottom right diagonal
    if 0 <= row + 1 < len(matrix) and 0 <= col + 1 < len(matrix):
        if matrix[row + 1][col + 1] == '*':
            counter += 1

    return counter


size = int(input())
matrix = [[None for _ in range(size)] for _ in range(size)]

bombs_count = int(input())
bombs_coordinates = []

for _ in range(bombs_count):
    mines = input()
    current_coord = coordinates = [int(el) for el in mines[1:-1].split(", ")]
    row, col = int(current_coord[0]), int(current_coord[1])
    bombs_coordinates.append((row, col))

for coordinate in bombs_coordinates:
    current_row = coordinate[0]
    current_col = coordinate[1]
    matrix[current_row][current_col] = '*'

for row in range(size):
    for col in range(size):
        if matrix[row][col] is None:
            matrix[row][col] = calculate_position(row, col, matrix)


for el in matrix:
    print(*el, sep=' ')
