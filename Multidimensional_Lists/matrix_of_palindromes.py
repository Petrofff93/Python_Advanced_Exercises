rows, cols = [int(x) for x in input().split()]

matrix = []


for row in range(rows):
    current_cipher = []
    for col in range(cols):
        current_cipher.append(f'{chr(97+row)}{chr(97+row+col)}{chr(97+row)}')
    matrix.append(current_cipher)

for ele in matrix:
    print(*ele, sep=' ')
