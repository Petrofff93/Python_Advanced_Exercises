m = int(input())
matrix = []

for _ in range(m):
    matrix.extend([int(x) for x in input().split(', ')])

print(matrix)
