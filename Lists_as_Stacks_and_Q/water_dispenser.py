from collections import deque

water_capacity = int(input())
people_q = deque()

while True:
    command = input()
    if not command == 'Start':
        people_q.append(command)
    else:
        break

command = input().split()

while not command[0] == 'End':
    if command[0].isdigit():
        current_int = int(command[0])
        person = people_q.popleft()
        if current_int <= water_capacity:
            print(f"{person} got water")
            water_capacity -= current_int
        else:
            print(f"{person} must wait")
    if command[0] == 'refill':
        water_capacity += int(command[1])

    command = input().split()

print(f"{water_capacity} liters left")



