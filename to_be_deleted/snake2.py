rows, cols = [int(x) for x in input().split()]
snake = input()
idx = 0

for row in range(rows):
    elements = [None] * cols
    if row % 2 == 0:
        for col in range(cols):
            elements[col] = snake[idx % len(snake)]
            idx += 1
    else:
        for col in range(cols - 1, -1, -1):
            elements[col] = snake[idx % len(snake)]
            idx += 1

    print(''.join(elements))