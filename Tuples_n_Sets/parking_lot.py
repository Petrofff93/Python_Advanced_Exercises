commands_count = int(input())
parking_lot = set()

for _ in range(commands_count):
    command, car_nr = input().split(', ')

    if command == 'IN':
        parking_lot.add(car_nr)
    else:
        parking_lot.remove(car_nr)

if not parking_lot:
    print("Parking Lot is Empty")
else:
    for car in parking_lot:
        print(car)
        