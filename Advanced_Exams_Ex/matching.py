from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
    male = males.pop()
    female = females.popleft()

    if male <= 0:
        females.appendleft(female)

    elif female <= 0:
        males.append(male)

    elif male % 25 == 0:
        males.pop()
        females.appendleft(female)

    elif female % 25 == 0:
        females.popleft()
        males.append(male)

    elif male == female:
        matches += 1

    else:
        males.append(male - 2)

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(str(y) for y in females)}")
else:
    print("Females left: none")

