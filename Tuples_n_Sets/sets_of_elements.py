a, b = [int(x) for x in input().split()]

first_set = set()
second_set = set()

for _ in range(a):
    current_num = int(input())
    first_set.add(current_num)

for _ in range(b):
    current_num = int(input())
    second_set.add(current_num)


result = first_set.intersection(second_set)
print(*result, sep='\n')
