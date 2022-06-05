def get_white_pos(white_row, white_col):
    return white_row - 1, white_col


def get_black_pos(black_row, black_col):
    return black_row + 1, black_col


size = 8
chess_board = []

black_row = 0
black_col = 0

white_row = 0
white_col = 0

rows_dict = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
cols_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

for row in range(size):
    current_element = input().split()
    for col in range(size):
        if current_element[col] == 'b':
            black_row = row
            black_col = col
        elif current_element[col] == 'w':
            white_row = row
            white_col = col
    chess_board.append(current_element)

while True:
    if 0 <= white_row - 1 < size and 0 <= white_col - 1 < size:
        if chess_board[white_row - 1][white_col - 1] == 'b':
            print(f'Game over! White win, capture on {cols_dict[white_col - 1]}{rows_dict[white_row - 1]}.')
            break
    if 0 <= white_row - 1 < size and 0 <= white_col + 1 < size:
        if chess_board[white_row - 1][white_col + 1] == 'b':
            print(f'Game over! White win, capture on {cols_dict[white_col + 1]}{rows_dict[white_row - 1]}.')
            break
    chess_board[white_row][white_col] = "-"
    white_row, white_col = get_white_pos(white_row, white_col)
    chess_board[white_row][white_col] = "w"
    if white_row == 0:
        print(f'Game over! White pawn is promoted to a queen at {cols_dict[white_col]}{rows_dict[white_row]}.')
        break

    if 0 <= black_row + 1 < size and 0 <= black_col - 1 < size:
        if chess_board[black_row + 1][black_col - 1] == 'w':
            print(f'Game over! Black win, capture on {cols_dict[black_col - 1]}{rows_dict[black_row + 1]}.')
            break

    if 0 <= black_row + 1 < size and 0 <= black_col + 1 < size:
        if chess_board[black_row + 1][black_col + 1] == 'w':
            print(f'Game over! Black win, capture on {cols_dict[black_col + 1]}{rows_dict[black_row + 1]}.')
            break
    chess_board[black_row][black_col] = "-"
    black_row, black_col = get_black_pos(black_row, black_col)
    chess_board[black_row][black_col] = "b"
    if black_row == 7:
        print(f'Game over! Black pawn is promoted to a queen at {cols_dict[black_col]}{rows_dict[black_row]}.')
        break
