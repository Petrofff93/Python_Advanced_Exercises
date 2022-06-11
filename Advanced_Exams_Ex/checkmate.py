def is_valid_pos(matrix, queen_row, queen_col):
    return 0 <= queen_row < len(matrix) and 0 <= queen_col < len(matrix)


def can_reach_king(*args):
    def queen_left_move(matrix, queen_row, queen_col):
        queen_col -= 1

        while is_valid_pos(matrix, queen_row, queen_col):
            if matrix[queen_row][queen_col] == 'Q':
                break
            elif matrix[queen_row][queen_col] == 'K':
                return True

            queen_col -= 1
        return False

    def queen_right_move(matrix, queen_row, queen_col):
        queen_col += 1
        while is_valid_pos(matrix, queen_row, queen_col):
            if matrix[queen_row][queen_col] == 'Q':
                break
            elif matrix[queen_row][queen_col] == 'K':
                return True

            queen_col += 1
        return False

    def queen_up_move(matrix, queen_row, queen_col):
        queen_row -= 1
        while is_valid_pos(matrix, queen_row, queen_col):
            if matrix[queen_row][queen_col] == 'Q':
                break
            elif matrix[queen_row][queen_col] == 'K':
                return True

            queen_row -= 1
        return False

    def queen_down_move(matrix, queen_row, queen_col):
        queen_row += 1
        while is_valid_pos(matrix, queen_row, queen_col):
            if matrix[queen_row][queen_col] == 'Q':
                break
            elif matrix[queen_row][queen_col] == 'K':
                return True

            queen_row += 1
        return False

    def queen_upper_left_move(matrix, queen_row, queen_col):
        queen_row -= 1
        queen_col -= 1
        while is_valid_pos(matrix, queen_row, queen_col):
            if matrix[queen_row][queen_col] == 'Q':
                break
            elif matrix[queen_row][queen_col] == 'K':
                return True

            queen_row -= 1
            queen_col -= 1
        return False

    def queen_upper_right_move(matrix, queen_row, queen_col):
        queen_row -= 1
        queen_col += 1
        while is_valid_pos(matrix, queen_row, queen_col):
            if matrix[queen_row][queen_col] == 'Q':
                break
            elif matrix[queen_row][queen_col] == 'K':
                return True

            queen_row -= 1
            queen_col += 1
        return False

    def queen_bottom_left_move(matrix, queen_row, queen_col):
        queen_row += 1
        queen_col -= 1
        while is_valid_pos(matrix, queen_row, queen_col):
            if matrix[queen_row][queen_col] == 'Q':
                break
            elif matrix[queen_row][queen_col] == 'K':
                return True

            queen_row += 1
            queen_col -= 1
        return False

    def queen_bottom_right_move(matrix, queen_row, queen_col):
        queen_row += 1
        queen_col += 1
        while is_valid_pos(matrix, queen_row, queen_col):
            if matrix[queen_row][queen_col] == 'Q':
                break
            elif matrix[queen_row][queen_col] == 'K':
                return True

            queen_row += 1
            queen_col += 1
        return False

    if queen_left_move(matrix, queen_row, queen_col) or queen_right_move(matrix, queen_row, queen_col) or\
            queen_bottom_right_move(matrix, queen_row, queen_col) or\
            queen_bottom_left_move(matrix, queen_row, queen_col) or queen_up_move(matrix, queen_row, queen_col) or\
            queen_down_move(matrix, queen_row, queen_col) or queen_upper_right_move(matrix, queen_row, queen_col) or\
            queen_upper_left_move(matrix, queen_row, queen_col):
        return True
    return False

size = 8
matrix = []

queens_positions = []
is_dead = False

for row in range(size):
    current_element = input().split()
    for col in range(size):
        if current_element[col] == 'Q':
            queens_positions.append([row, col])
    matrix.append(current_element)

while queens_positions:
    current_queen = queens_positions.pop()
    queen_row, queen_col = current_queen
    if can_reach_king(matrix, queen_row, queen_col):
        is_dead = True
        print(current_queen)

if not is_dead:
    print('The king is safe!')
