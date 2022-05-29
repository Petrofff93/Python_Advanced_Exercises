n = int(input())
matrix = []

for _ in range(n):
    current_element = [int(x) for x in input().split()]
    matrix.append(current_element)

while True:
    line = input().split()
    if line[0] == 'END':
        for item in matrix:
            print(*item, sep=' ')
        break

    command = line[0]
    row, col, value = [int(x) for x in line[1:]]

    if 0 > row or row >= len(matrix) or 0 > col or col >= len(matrix):
        print('Invalid coordinates')
        continue

    if command == 'Add':
        matrix[row][col] += value
    elif command == 'Subtract':
        matrix[row][col] -= value

