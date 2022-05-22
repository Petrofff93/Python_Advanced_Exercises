n = int(input())

periodic_table_set = set()

for _ in range(n):
    [periodic_table_set.add(x) for x in input().split()]

print(*periodic_table_set, sep='\n')
