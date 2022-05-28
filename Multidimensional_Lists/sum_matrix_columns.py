rows_count, column_count = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows_count):
    matrix.append([int(x) for x in input().split()])

result = []

for column_idx in range(column_count):
    column_sum = 0
    for row_idx in range(rows_count):
        column_sum += matrix[row_idx][column_idx]
    result.append(column_sum)

[print(x) for x in result]



