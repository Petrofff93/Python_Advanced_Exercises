def valid_coordinates(coordinates, rows, cols):
    if len(coordinates) != 4:
        return False
    row1, col1, row2, col2 = coordinates
    if 0 > row1 or row1 >= rows or 0 > col1 or col1 >= cols or 0 > row2 or row2 >= rows or 0 > col2 >= cols:
        return False

    return True


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    line = input().split()
    if line[0] == 'END':
        break

    command = line[0]
    coordinates = [int(x) for x in line[1:]]
    if valid_coordinates(coordinates, rows, cols) and command == 'swap':
        row1, col1, row2, col2 = coordinates
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for el in matrix:
            print(*el, sep=' ')
    else:
        print('Invalid input!')
