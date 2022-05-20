names_count = int(input())
name_set = set()

for _ in range(names_count):
    name_set.add(input())

for item in name_set:
    print(item)
    