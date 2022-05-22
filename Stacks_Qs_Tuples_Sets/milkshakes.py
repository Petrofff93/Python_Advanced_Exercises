from collections import deque

chocolates_stack = [int(x) for x in input().split(', ')]
cups_of_milk_q = deque(int(x) for x in input().split(', '))

milkshakes_count = 0
is_done = False


while True:
    if milkshakes_count == 5:
        is_done = True
        break

    if not chocolates_stack:
        break
    if not cups_of_milk_q:
        break

    current_chocolate = chocolates_stack[-1]
    current_milk = cups_of_milk_q[0]

    if current_chocolate <= 0 and current_milk <= 0:
        cups_of_milk_q.popleft()
        chocolates_stack.pop()
        continue

    if current_milk <= 0:
        cups_of_milk_q.popleft()
        continue
    if current_chocolate <= 0:
        chocolates_stack.pop()
        continue

    if current_milk == current_chocolate:
        chocolates_stack.pop()
        cups_of_milk_q.popleft()
        milkshakes_count += 1
    else:
        cups_of_milk_q.append(cups_of_milk_q.popleft())
        chocolates_stack[-1] -= 5

if is_done:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates_stack:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates_stack])}")
else:
    print('Chocolate: empty')

if cups_of_milk_q:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk_q])}")
else:
    print('Milk: empty')
