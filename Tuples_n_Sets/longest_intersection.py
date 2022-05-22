n = int(input())

first_set = set()
second_set = set()
longest_intersection = set()

for _ in range(n):
    first, second = input().split('-')
    first_start, first_end = [int(x) for x in first.split(',')]
    second_start, second_end = [int(x) for x in second.split(',')]

    for x in range(first_start, first_end + 1):
        first_set.add(x)
    for x in range(second_start, second_end + 1):
        second_set.add(x)

    result = first_set.intersection(second_set)
    if len(result) > len(longest_intersection):
        longest_intersection = result

    first_set = set()
    second_set = set()

print(f'Longest intersection is [{", ".join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}')
