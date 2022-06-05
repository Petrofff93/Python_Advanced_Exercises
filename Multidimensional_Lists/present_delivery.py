def get_next_position(santa_row, santa_col, direction):
    if direction == 'up':
        return santa_row - 1, santa_col
    elif direction == 'down':
        return santa_row + 1, santa_col
    elif direction == 'left':
        return santa_row, santa_col - 1
    elif direction == 'right':
        return santa_row, santa_col + 1


def santa_cookies(santa_row, santa_col):
    possible_directions = [
        (santa_row, santa_col - 1),
        (santa_row, santa_col + 1),
        (santa_row + 1, santa_col),
        (santa_row - 1, santa_col)
    ]
    return possible_directions


presents_count = int(input())
size = int(input())
matrix = []

nice_kids = 0
santa_row = 0
santa_col = 0

for row in range(size):
    current_element = input().split()
    for col in range(size):
        if current_element[col] == 'S':
            santa_row = row
            santa_col = col
        elif current_element[col] == 'V':
            nice_kids += 1
    matrix.append(current_element)

happy_kids = nice_kids
while presents_count > 0:
    direction = input()

    if direction == 'Christmas morning':
        break
    matrix[santa_row][santa_col] = '-'
    santa_row, santa_col = get_next_position(santa_row, santa_col, direction)

    if matrix[santa_row][santa_col] == 'V':
        presents_count -= 1
        nice_kids -= 1
        matrix[santa_row][santa_col] = 'S'
    elif matrix[santa_row][santa_col] == 'X':
        matrix[santa_row][santa_col] = 'S'
    elif matrix[santa_row][santa_col] == 'C':
        matrix[santa_row][santa_col] = 'S'
        result = santa_cookies(santa_row, santa_col)
        for r, c in result:
            if presents_count == 0:
                break
            if matrix[r][c] == 'V':
                nice_kids -= 1
                presents_count -= 1
            elif matrix[r][c] == 'X':
                presents_count -= 1
            matrix[r][c] = '-'

    matrix[santa_row][santa_col] = 'S'

if nice_kids == 0 and presents_count >= 0:
    for el in matrix:
        print(*el, sep=' ')
    print(f'Good job, Santa! {happy_kids} happy nice kid/s.')
elif nice_kids > 0 and presents_count <= 0:
    print(f'Santa ran out of presents!')
    for el in matrix:
        print(*el, sep=' ')
    print(f'No presents for {nice_kids} nice kid/s.')
elif nice_kids > 0 and presents_count > 0:
    for el in matrix:
        print(*el, sep=' ')
    print(f'No presents for {nice_kids} nice kid/s.')
