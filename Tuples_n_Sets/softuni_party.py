number_of_guests = int(input())
regular_guest = set()
vip_guest = set()


def is_vip(guest):
    return guest[0].isdigit()


for _ in range(number_of_guests):
    current_guest = input()

    if is_vip(current_guest):
        vip_guest.add(current_guest)
    else:
        regular_guest.add(current_guest)

while True:
    guest = input()

    if guest == 'END':
        break

    if is_vip(guest):
        vip_guest.remove(guest)
    else:
        regular_guest.remove(guest)

print(len(vip_guest) + len(regular_guest))
[print(guest) for guest in sorted(vip_guest)]
[print(guest) for guest in sorted(regular_guest)]
