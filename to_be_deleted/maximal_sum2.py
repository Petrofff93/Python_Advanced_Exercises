def current_best(matrix, row, col, rows, cols):
    if 0 <= row + 1 < rows and row + 2 < rows and 0 <= col + 1 < cols and col + 2 < cols:
        current_matrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                          [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                          [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]
        current_sum = sum(sum(current_matrix, []))
        return current_matrix, current_sum


rows, cols = [int(x) for x in input().split()]
matrix = []
best_matrix = []
best_sum = float('-inf')

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows):
    for col in range(cols):
        try:
            current_matrix, result = current_best(matrix, row, col, rows, cols)
            if result > best_sum:
                best_sum = result
                best_matrix = current_matrix
        except TypeError:
            continue

print(f'Sum = {best_sum}')

for element in best_matrix:
    print(*element, sep=' ')

