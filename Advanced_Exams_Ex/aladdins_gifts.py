from collections import deque


def is_gift_made(mix_result):
    if 100 <= mix_result <= 199:
        return 'Gemstone'
    elif 200 <= mix_result <= 299:
        return 'Porcelain Sculpture'
    elif 300 <= mix_result <= 399:
        return 'Gold'
    elif 400 <= mix_result <= 499:
        return 'Diamond Jewellery'


materials_s = [int(x) for x in input().split()]
magic_level_q = deque(int(x) for x in input().split())

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials_s and magic_level_q:
    current_material = materials_s.pop()
    current_magic = magic_level_q.popleft()
    mix_result = current_magic + current_material

    if mix_result < 100:
        if mix_result % 2 == 0:
            mix_result = (current_material * 2) + (current_magic * 3)
        else:
            mix_result = (current_material * 2) + (current_magic * 2)

    if mix_result > 499:
        mix_result = mix_result // 2

    mixed_gift = is_gift_made(mix_result)

    if mixed_gift:
        gifts[mixed_gift] += 1


if gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0 or gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials_s:
    print(f'Materials left: {", ".join(str(x) for x in materials_s)}')
if magic_level_q:
    print(f'Magic left: {", ".join(str(x) for x in magic_level_q)}')


for key, value in sorted(gifts.items()):
    if value > 0:
        print(f'{key}: {value}')



