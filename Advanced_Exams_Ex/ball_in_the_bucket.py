from collections import deque


def is_valid_shoot(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def bucket_point_collect(matrix, row, col):
    result = 0

    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if c == col and matrix[r][c].isdigit():
                result += int(matrix[r][c])
    return result


def final_res_func(score):
    if 100 <= score <= 199:
        return 'Football'
    elif 200 <= score <= 299:
        return 'Teddy Bear'
    elif score >= 300:
        return 'Lego Construction Set'


size = 6
score = 0

matrix = []
throw_coords = deque()

for row in range(size):
    matrix.append(input().split())

for _ in range(3):
    row, col = input().split(', ')
    throw_coords.append([int(row[1:]), int(col[0:-1])])

while throw_coords:
    row, col = throw_coords.popleft()

    if not is_valid_shoot(row, col, matrix):
        continue

    if matrix[row][col] != 'B':
        continue

    score += bucket_point_collect(matrix, row, col)
    matrix[row][col] = 0

prize = final_res_func(score)

if score < 100:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
else:
    print(f"Good job! You scored {score} points, and you've won {prize}.")
