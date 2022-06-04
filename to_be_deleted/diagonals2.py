n = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for i in range(n):
    current_element = [int(x) for x in input().split(', ')]
    primary_diagonal.append(current_element[i])
    secondary_diagonal.append(current_element[n - i - 1])

print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')
