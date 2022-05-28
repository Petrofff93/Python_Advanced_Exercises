square_rows = int(input())

matrix = [[int(x) for x in input().split(' ')] for _ in range(square_rows)]
primary_diagonal = []
secondary_diagonal = []

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][square_rows - i - 1])

result = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(result)
