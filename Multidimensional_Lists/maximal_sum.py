rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    current_element = [int(x) for x in input().split()]
    matrix.append(current_element)


def valid_matrix(row, col, matrix, rows, cols):
    if row + 1 < rows and col + 1 < cols and row + 2 < rows and col + 2 < cols:
        result = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                  [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                  [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]

        return result


max_sum = float('-inf')
biggest_matrix = []

for row in range(rows):
    for col in range(cols):
        current_result = valid_matrix(row, col, matrix, rows, cols)
        if current_result is None:
            continue
        if sum(sum(current_result, [])) > max_sum:
            max_sum = sum(sum(current_result, []))
            if biggest_matrix:
                biggest_matrix = []
                biggest_matrix.extend(current_result)
            else:
                biggest_matrix.extend(current_result)

print(f'Sum = {max_sum}')
for ele in biggest_matrix:
    print(*ele, sep=' ')



