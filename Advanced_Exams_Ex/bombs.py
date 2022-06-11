from collections import deque

bomb_effect = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

possible_bombs = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120
}

created_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

is_done = False
while bomb_effect and bomb_casings:

    current_effect = bomb_effect[0]
    current_casing = bomb_casings[-1]

    current_bomb_sum = current_effect + current_casing

    if created_bombs['Datura Bombs'] > 2 and created_bombs['Cherry Bombs'] > 2 \
            and created_bombs['Smoke Decoy Bombs'] > 2:
        print('Bene! You have successfully filled the bomb pouch!')
        is_done = True
        break

    is_bomb = True
    for bomb, value in possible_bombs.items():
        if value == current_bomb_sum:
            bomb_effect.popleft()
            bomb_casings.pop()
            created_bombs[bomb] += 1
            is_bomb = False

    if is_bomb:
        bomb_casings[-1] -= 5


if not is_done:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f'Bomb Effects: {", ".join([str(x) for x in bomb_effect])}')
else:
    print('Bomb Effects: empty')

if bomb_casings:
    print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casings])}')
else:
    print('Bomb Casings: empty')

for bomb, count in sorted(created_bombs.items()):
    print(f'{bomb}: {count}')
