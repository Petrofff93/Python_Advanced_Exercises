from itertools import combinations

sequence = [int(x) for x in input().split()]
target = int(input())

my_set = set()
iterations = 0

for num1, num2 in combinations(sequence, 2):
    if num1 + num2 == target:
        iterations += 1
        my_set.add((num1, num2))
        print(f"{num1} + {num2} = {target}")
    else:
        iterations += 1

print(f"Iterations done: {iterations}")
if my_set:
    print(*my_set, sep='\n')
