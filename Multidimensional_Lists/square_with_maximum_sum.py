rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

sub_matrix = []

for row in range(rows):
    for col in range(cols):
        result = []
        if 0 <= row < rows and 0 <= col < cols:
            result.append(matrix[row][col])
        if 0 <= col + 1 < cols and 0 <= row < rows:
            result.append(matrix[row][col + 1])
        if 0 <= row + 1 < rows:
            result.append(matrix[row + 1][col])
        if 0 <= row + 1 < rows and 0 <= col + 1 < cols:
            result.append(matrix[row + 1][col + 1])
        if len(result) == 4:
            sub_matrix.append(result)

total_sum = 0
final_matrix = []

for el in sub_matrix:
    if sum(el) > total_sum:
        total_sum = sum(el)
        if final_matrix:
            final_matrix.pop()
            final_matrix.append(el)
        else:
            final_matrix.append(el)

print(f'{final_matrix[0][0]} {final_matrix[0][1]}\n{final_matrix[0][2]} {final_matrix[0][3]}')
print(total_sum)


