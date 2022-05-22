from collections import deque, defaultdict

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

presents_crafted = defaultdict(int)

while materials and magic:
    curr_material = materials.pop()
    curr_magic = magic.popleft()
    result = curr_material * curr_magic

    if result in presents:
        presents_crafted[presents[result]] += 1
        continue

    if result < 0:
        materials.append(curr_material + curr_magic)
    elif result > 0:
        materials.append(curr_material + 15)
    elif result == 0:
        if curr_material != 0:
            materials.append(curr_material)
        elif curr_magic != 0:
            magic.appendleft(curr_magic)

if 'Doll' in presents_crafted and 'Wooden train' in presents_crafted:
    print('The presents are crafted! Merry Christmas!')
elif 'Teddy bear' in presents_crafted and 'Bicycle' in presents_crafted:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if materials:
    print(f'Materials left: {", ".join(str(i) for i in reversed(materials))}')
if magic:
    print(f'Magic left: {", ".join(str(i) for i in magic)}')

[print(f'{key}: {value}') for key, value in sorted(presents_crafted.items())]
