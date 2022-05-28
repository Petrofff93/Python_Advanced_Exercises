n, m = [int(x) for x in input().split(', ')]
matrix = []
total_sum = 0

for _ in range(n):
    current_row = [int(x) for x in input().split(', ')]
    total_sum += sum(current_row)
    matrix.append(current_row)

print(total_sum)
print(matrix)



