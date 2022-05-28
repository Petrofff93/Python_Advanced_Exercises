rows, cols = [int(x) for x in input().split()]

matrix = []
total_identical = 0

for _ in range(rows):
    current_input = input().split()
    matrix.append(current_input)


def is_valid(row, col, matrix, rows, cols):
    if 0 <= row < rows and 0 <= col < cols and row + 1 < rows and col + 1 < cols:
        result = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]
        return result


for row in range(rows):
    for col in range(cols):
        current_res = is_valid(row, col, matrix, rows, cols)
        if current_res is not None:
            if len(current_res) == len([x for x in current_res if x == current_res[0]]):
                total_identical += 1

print(total_identical)


