size = int(input())

wonderland_matrix = []
alice_row = 0
alice_col = 0
tea_bags = 0

directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

for row in range(size):
    current_element = input().split()
    for col in range(size):
        if current_element[col] == 'A':
            alice_row = row
            alice_col = col
    wonderland_matrix.append(current_element)

while True:
    if tea_bags >= 10:
        print('She did it! She went to the party.')
        for el in wonderland_matrix:
            print(*el, sep=' ')

        break

    command = input()
    row, col = directions[command](alice_row, alice_col)
    wonderland_matrix[alice_row][alice_col] = '*'
    alice_row, alice_col = row, col

    if alice_row < 0 or alice_row >= size or alice_col < 0 or alice_col >= size:
        print("Alice didn't make it to the tea party.")
        for el in wonderland_matrix:
            print(*el, sep=' ')

        break

    if wonderland_matrix[alice_row][alice_col] == 'R':
        wonderland_matrix[alice_row][alice_col] = '*'
        print("Alice didn't make it to the tea party.")
        for el in wonderland_matrix:
            print(*el, sep=' ')

        break

    if wonderland_matrix[alice_row][alice_col] != '.' and wonderland_matrix[alice_row][alice_col] != '*':
        tea_bags += int(wonderland_matrix[alice_row][alice_col])
        wonderland_matrix[alice_row][alice_col] = '*'
