from collections import deque

petrol_pumps = int(input())
pump_q = deque(list())
tank = 0
my_att = False


for _ in range(petrol_pumps):
    current_pump = list(map(int, input().split()))
    pump_q.append(current_pump)

for attempt in range(petrol_pumps):
    for item in pump_q:
        tank += item[0]
        if tank >= item[1]:
            tank -= item[1]
            my_att = True
        else:
            pump_q.rotate(-1)
            tank = 0
            my_att = False
            break
    if my_att:
        print(attempt)
        break

