n = int(input())
names_set = set()

for _ in range(n):
    current_name = input()
    names_set.add(current_name)

print(*names_set, sep='\n')
