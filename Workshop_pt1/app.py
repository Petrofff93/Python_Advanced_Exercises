from collections import deque


def create_board(*args):
    board = [[0 for _ in range(*args)] for _ in range(*args)]
    return board


def print_board(field):
    for el in field:
        print(el)


def is_valid_col(current_col, board):
    return 0 <= current_col - 1 < len(board)


def current_player_turn(current_col, board, current_player):
    if is_valid_col(current_col, board):
        current_col = current_col - 1

        while True:
            for i in range(len(board) - 1, -1, -1):
                if board[i][current_col] == 0:
                    board[i][current_col] = current_player
                    return board, i, current_col
            if current_col + 1 < len(board):
                current_col += 1
            else:
                current_col = 0


players = deque([1, 2])
board_size = int(input('Please enter the board size (number between 5-10) '))
board = create_board(board_size)
print_board(board)


def player_won(board, current_player, row, col):
    while True:
        if 0 <= row - 1 < len(board) and 0 <= row - 2 < len(board) and 0 <= row - 3 < len(board):
            if board[row - 1][col] == board[row - 2][col] == board[row - 3][col] == board[row][col] == current_player:
                return True
            else:
                return False

        elif 0 <= col - 1 < len(board) and 0 <= col - 2 < len(board) and 0 <= col - 3 < len(board):
            if board[row][col] == board[row][col - 1] == board[row][col - 2] == board[row][col - 3] == current_player:
                return True
            else:
                return False


def is_draw(board):
    pass


while True:
    current_player = players[0]
    current_col = int(input(f'Player {current_player}, please choose a column (between 0 and size - 1) '))
    board, row, col = current_player_turn(current_col, board, current_player)

    if player_won(board, current_player, row, col):
        print_board(board)
        print(f'Player {current_player} won! END OF GAME!')
        break

    if is_draw(board):
        if all(board) != 0:
            print_board(board)
            print("Nobody wins! It's a draw!")
            break

    print_board(board)
    players.append(players.popleft())
