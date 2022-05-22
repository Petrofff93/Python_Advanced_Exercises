n = int(input())
odd_set = set()
even_set = set()
result = 0

for row in range(1, n + 1):
    current_name = input()

    for el in current_name:
        result += ord(el)

    result = result // row

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

    result = 0

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if even_sum == odd_sum:
    result = even_set.union(odd_set)

elif odd_sum > even_sum:
    result = odd_set.difference(even_set)

else:
    result = even_set.symmetric_difference(odd_set)

print(*result, sep=', ')
