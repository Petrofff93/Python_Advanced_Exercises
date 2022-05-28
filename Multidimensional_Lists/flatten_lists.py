my_input = [x.strip() for x in input().split('|')]

result = []

for idx in range(len(my_input) - 1, -1, -1):
    current_el = my_input[idx].strip().split()
    result.extend(current_el)

print(*result)


