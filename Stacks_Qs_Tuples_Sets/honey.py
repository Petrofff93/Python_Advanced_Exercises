from collections import deque

bees_stack = deque(int(x) for x in input().split())
nectar_q = [int(x) for x in input().split()]
making_symbols = deque(x for x in input().split())

total_honey = 0

while bees_stack and nectar_q:
    current_bee = bees_stack.popleft()
    current_nectar = nectar_q.pop()

    if current_nectar >= current_bee:
        current_operation = making_symbols.popleft()
        if current_operation == '+':
            total_honey += abs(current_bee + current_nectar)
        elif current_operation == '-':
            total_honey += abs(current_bee - current_nectar)
        elif current_operation == '*':
            total_honey += abs(current_bee * current_nectar)
        elif current_operation == '/':
            try:
                total_honey += abs(current_bee / current_nectar)
            except ZeroDivisionError:
                continue
    else:
        bees_stack.appendleft(current_bee)


print(f"Total honey made: {total_honey}")

if bees_stack:
    print(f"Bees left: {', '.join([str(x) for x in bees_stack])}")

if nectar_q:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_q])}")
