rows = int(input())
bomb_matrix = []

for _ in range(rows):
    current_cells = [int(x) for x in input().split()]
    bomb_matrix.append(current_cells)

bomb_coordinates = [x for x in input().split()]


def get_children(bomb_matrix, row, col):
    possible_cords = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1]
    ]
    result = []
    for child_row, child_col in possible_cords:
        if 0 <= child_row < len(bomb_matrix) and 0 <= child_col < len(bomb_matrix) and bomb_matrix[child_row][
            child_col] > 0:
            result.append([child_row, child_col])
    return result


for bomb in bomb_coordinates:
    row, col = [int(x) for x in bomb.split(',')]
    power = bomb_matrix[row][col]

    if power <= 0:
        continue

    bomb_matrix[row][col] = 0

    children = get_children(bomb_matrix, row, col)
    for child_row, child_col in children:
        bomb_matrix[child_row][child_col] -= power

active_cells = 0
active_cells_sum = 0

for row in bomb_matrix:
    for el in row:
        if el > 0:
            active_cells += 1
            active_cells_sum += el

print(f'Alive cells: {active_cells}')
print(f'Sum: {active_cells_sum}')
for row in bomb_matrix:
    print(*row, sep=' ')
