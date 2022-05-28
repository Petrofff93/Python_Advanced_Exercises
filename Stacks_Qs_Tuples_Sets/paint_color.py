from collections import deque

words = deque(input().split())

primary_colors = {'red', 'yellow', 'blue'}
secondary_colors = {
        'orange': ['red', 'yellow'],
        'purple': ['red', 'blue'],
        'green': ['yellow', 'blue']
}

collected_colors = []


while words:
    left = words.popleft()
    right = words.pop() if words else ''

    result = left + right
    if result in primary_colors or result in secondary_colors.keys():
        collected_colors.append(result)
        continue

    result = right + left
    if result in primary_colors or result in secondary_colors.keys():
        collected_colors.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        words.insert(len(words) // 2, left)
    if right:
        words.insert(len(words) // 2, right)

for k, v in secondary_colors.items():
    if k in collected_colors:
        if v[0] not in collected_colors or v[1] not in collected_colors:
            collected_colors.remove(k)

print(collected_colors)
