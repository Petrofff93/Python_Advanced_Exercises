from collections import deque

field_size = int(input())
directions = deque([x for x in input().split()])

mining_field = []
coal_count = 0
miner_row = 0
miner_col = 0
is_ended = True

for _ in range(field_size):
    mining_field.append([x for x in input().split()])

for row in range(field_size):
    for col in range(field_size):
        if mining_field[row][col] == 's':
            miner_row, miner_col = row, col
        elif mining_field[row][col] == 'c':
            coal_count += 1


def valid_move(miner_row, miner_col, mining_field, current_direction):
    result = []
    if current_direction == 'up':
        if 0 <= miner_row - 1 < len(mining_field):
            result = [miner_row - 1, miner_col]
            return result

    elif current_direction == 'down':
        if 0 <= miner_row + 1 < len(mining_field):
            result = [miner_row + 1, miner_col]
            return result

    elif current_direction == 'left':
        if 0 <= miner_col - 1 < len(mining_field):
            result = [miner_row, miner_col - 1]
            return result

    elif current_direction == 'right':
        if 0 <= miner_col + 1 < len(mining_field):
            result = [miner_row, miner_col + 1]
            return result


while directions:
    current_direction = directions.popleft()
    if valid_move(miner_row, miner_col, mining_field, current_direction):
        mining_field[miner_row][miner_col] = '*'
        miner_row, miner_col = valid_move(miner_row, miner_col, mining_field, current_direction)
        if mining_field[miner_row][miner_col] == 'c':
            coal_count -= 1
            mining_field[miner_row][miner_col] = 's'
            if coal_count == 0:
                print(f'You collected all coal! ({miner_row}, {miner_col})')
                is_ended = False
                break
        elif mining_field[miner_row][miner_col] == 'e':
            print(f'Game over! ({miner_row}, {miner_col})')
            is_ended = False
            break
        mining_field[miner_row][miner_col] = 's'

if is_ended:
    print(f"{coal_count} pieces of coal left. ({miner_row}, {miner_col})")
