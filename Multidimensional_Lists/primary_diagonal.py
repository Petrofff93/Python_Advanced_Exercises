# First variant
# n = int(input())
#
# matrix = []
# result = 0
#
# for i in range(n):
#     current_row = [int(x) for x in input().split()]
#     matrix.append(current_row)
#     result += current_row[i]
#
# print(result)


n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

result = 0

for idx in range(n):
    result += matrix[idx][idx]

print(result)




