from collections import deque

materials_stack = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())
toys_crafted = {}
total_magic = 0

toys_dict = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400
}

while magic_level and materials_stack:

    current_material = materials_stack[-1]
    current_magic_level = magic_level[0]

    if current_material == 0 and current_magic_level == 0:
        materials_stack.pop()
        magic_level.popleft()
        continue

    if current_magic_level == 0:
        magic_level.popleft()
        continue

    if current_material == 0:
        materials_stack.pop()
        continue

    result = current_material * current_magic_level

    if result in toys_dict.values():
        materials_stack.pop()
        magic_level.popleft()

        for k, v in toys_dict.items():
            if v == result:
                if k in toys_crafted:
                    toys_crafted[k] += 1
                else:
                    toys_crafted[k] = 1
    else:
        if result < 0:
            result = current_material + current_magic_level
            materials_stack.pop()
            magic_level.popleft()
            materials_stack.append(result)
        elif result > 0:
            magic_level.popleft()
            materials_stack[-1] += 15
        elif result == 0:
            if current_material != 0:
                materials_stack.append(current_material)
            elif current_magic_level != 0:
                magic_level.appendleft(current_magic_level)


if 'Doll' and 'Wooden train' in toys_crafted:
    print('The presents are crafted! Merry Christmas!')
elif 'Teddy bear' and 'Bicycle' in toys_crafted:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials_stack:
    final_material = reversed(materials_stack)
    print(f"Materials left: {', '.join(str(x) for x in final_material)}")

if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for k, v in sorted(toys_crafted.items()):
    print(f"{k}: {v}")







