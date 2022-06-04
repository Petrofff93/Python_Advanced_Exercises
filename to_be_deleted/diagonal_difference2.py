n = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for i in range(n):
    current_element = [int(x) for x in input().split()]
    primary_diagonal.append(current_element[i])
    secondary_diagonal.append(current_element[n - i - 1])

primary = sum(primary_diagonal)
secondary = sum(secondary_diagonal)

print(abs(primary - secondary))

