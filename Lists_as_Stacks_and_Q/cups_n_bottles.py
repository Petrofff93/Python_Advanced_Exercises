from collections import deque

cups = deque([int(cup) for cup in input().split()])
bottles = [int(bottle) for bottle in input().split()]

wasted_water = 0

while cups and bottles:
    if bottles[-1] >= cups[0]:
        wasted_water += (bottles.pop() - cups.popleft())
    else:
        while cups[0] >= 0:
            cups[0] -= bottles.pop()
            break

if cups:
    print("Cups:", *cups)
else:
    print("Bottles:", *bottles)
print(f"Wasted litters of water: {wasted_water}")
