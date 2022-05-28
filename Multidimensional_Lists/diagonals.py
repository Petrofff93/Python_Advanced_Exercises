square_rows = int(input())

matrix = [[int(x) for x in input().split(',')] for _ in range(square_rows)]
primary_diagonal = []
secondary_diagonal = []

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][square_rows - i - 1])

print(f'Primary diagonal: {", ".join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')


