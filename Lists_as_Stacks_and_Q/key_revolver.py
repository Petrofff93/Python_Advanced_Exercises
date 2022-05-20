from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets_stack = [int(x) for x in input().split()]
locks_q = deque([int(x) for x in input().split()])
intelligence_price = int(input())

bullet_count = 0
count_in_barrel = 0
is_unlocked = True

while locks_q:

    if bullets_stack:
        current_bullet = bullets_stack.pop()
    else:
        print(f"Couldn't get through. Locks left: {len(locks_q)}")
        is_unlocked = False
        break

    current_lock = locks_q[0]
    count_in_barrel += 1

    if current_bullet <= current_lock:
        print('Bang!')
        locks_q.popleft()
    else:
        print('Ping!')

    if count_in_barrel == gun_barrel_size and bullets_stack:
        print('Reloading!')
        count_in_barrel = 0

    bullet_count += 1

if is_unlocked:
    money_earned = intelligence_price - bullet_count * bullet_price
    print(f"{len(bullets_stack)} bullets left. Earned ${money_earned}")