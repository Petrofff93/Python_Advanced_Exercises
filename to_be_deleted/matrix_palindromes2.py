rows, cols = [int(x) for x in input().split()]
matrix_of_palindromes = []

for row in range(rows):
    current_palindrome = []
    for col in range(cols):
        current_palindrome.append(f'{chr(97 + row)}{chr(97 + row + col)}{chr(97 + row)}')
    matrix_of_palindromes.append(current_palindrome)

for element in matrix_of_palindromes:
    print(*element, sep=' ')
