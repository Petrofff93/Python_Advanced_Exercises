clothes_stack = list(map(int, input().split()))
rack_capa = int(input())
current_rack_capa = rack_capa
rack_count = 1

while True:
    try:
        current_cloth = clothes_stack[-1]
    except IndexError:
        print(rack_count)
        break

    if current_rack_capa >= current_cloth:
        current_rack_capa -= current_cloth
        clothes_stack.pop()
    else:
        rack_count += 1
        current_rack_capa = rack_capa
