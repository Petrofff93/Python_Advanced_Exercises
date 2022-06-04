def is_valid_matrix(matrix, row, col, rows, cols):
    if 0 <= row + 1 < rows and 0 <= col + 1 < cols \
            and matrix[row][col] == matrix[row + 1][col] == matrix[row][col + 1] == matrix[row + 1][col + 1]:
        return True


rows, cols = [int(x) for x in input().split()]

matrix = []
sum_squares = 0

for _ in range(rows):
    matrix.append(input().split())

for row in range(rows):
    for col in range(cols):
        if is_valid_matrix(matrix, row, col, rows, cols):
            sum_squares += 1

print(sum_squares)

