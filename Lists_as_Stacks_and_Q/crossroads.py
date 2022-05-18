from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars_q = deque()
cars_passed = 0
is_crashed = False

total_green = green_light_duration + free_window_duration

while True:

    command = input()
    if command == 'END':
        break

    total_green = green_light_duration + free_window_duration

    if command == 'green':
        while cars_q:
            current_car = cars_q[0]
            if len(current_car) <= total_green:
                total_green -= len(current_car)
                cars_passed += 1
                cars_q.popleft()
                if total_green <= free_window_duration:
                    break
            else:
                idx = abs(len(current_car) - total_green)
                print('A crash happened!')
                print(f"{current_car} was hit at {current_car[-idx]}.")
                is_crashed = True
                break
        if is_crashed:
            break
    cars_q.append(command)

if not is_crashed:
    print('Everyone is safe.')
    print(f"{cars_passed} total cars passed the crossroads.")