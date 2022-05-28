rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])


def valid_command(command, rows, cols):
    if len(command) == 5 and command[0] == 'swap':
        row1, col1, row2, col2 = [int(x) for x in command[1:]]
        if 0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols:
            return True
    return False


while True:
    command = input().split()
    if command[0] == 'END':
        break

    if valid_command(command, rows, cols):
        row1, col1, row2, col2 = [int(x) for x in command[1:]]
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for ele in matrix:
            print(*ele, sep=' ')
    else:
        print('Invalid input!')

