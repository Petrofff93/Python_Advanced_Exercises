n = int(input())
matrix = []

for _ in range(n):
    matrix.append(input())

needed_symbol = input()
is_found = False

for i in range(n):
    if is_found:
        break
    for k in range(n):
        if matrix[i][k] == needed_symbol:
            is_found = True
            print(f'({i}, {k})')
            break

if not is_found:
    print(f'{needed_symbol} does not occur in the matrix')




