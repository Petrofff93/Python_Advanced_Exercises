from collections import deque

males_stack = [int(x) for x in input().split()]
females_q = deque([int(x) for x in input().split()])

matches_count = 0

while males_stack and females_q:
    current_female = females_q[0]
    current_male = males_stack[-1]

    if current_male <= 0:
        males_stack.pop()
        continue

    if current_female <= 0:
        females_q.popleft()
        continue

    if current_female % 25 == 0:
        females_q.popleft()
        try:
            females_q.popleft()
        except IndexError:
            pass
        continue

    if current_male % 25 == 0:
        males_stack.pop()
        try:
            males_stack.pop()
        except IndexError:
            pass
        continue

    if current_male == current_female:
        females_q.popleft()
        males_stack.pop()
        matches_count += 1
    else:
        females_q.popleft()
        males_stack[-1] -= 2

print(f'Matches: {matches_count}')

if males_stack:
    print(f'Males left: {", ".join(reversed([str(x) for x in males_stack]))}')
else:
    print('Males left: none')

if females_q:
    print(f"Females left: {', '.join(str(x) for x in females_q)}")
else:
    print('Females left: none')
