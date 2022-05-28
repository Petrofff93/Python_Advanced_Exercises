rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])


def is_valid(row, col, matrix, rows, cols):
    if 0 <= row < rows and 0 <= col < cols \
            and 0 <= col + 1 < cols and 0 <= row < rows and 0 <= row + 1 < rows \
            and 0 <= row + 1 < rows and 0 <= col + 1 < cols:
        return [[matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]]


result = []

for row in range(rows):
    for col in range(cols):
        current_check = is_valid(row, col, matrix, rows, cols)
        if current_check:
            result.extend(current_check)

total_sum = 0
final_matrix = []

for ele in result:
    if sum(ele) > total_sum:
        total_sum = sum(ele)
        if final_matrix:
            final_matrix.pop()
        final_matrix.append(ele)


print(f'{final_matrix[0][0]} {final_matrix[0][1]}\n{final_matrix[0][2]} {final_matrix[0][3]}')
print(total_sum)
