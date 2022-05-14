from collections import deque

food_qty = int(input())
orders = deque(list(map(int, input().split())))
print(max(orders))

while True:
    try:
        current_order = orders[0]
    except IndexError:
        print('Orders complete')
        break

    if food_qty >= current_order:
        food_qty -= current_order
        orders.popleft()
    else:
        if orders:
            print(f"Orders left: {' '.join(str(x) for x in orders)}")
            break

