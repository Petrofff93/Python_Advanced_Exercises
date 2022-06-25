from collections import deque

eggs_size = deque(int(x) for x in input().split(', '))
papers_size = [int(x) for x in input().split(', ')]

BOX_SIZE = 50

boxes_count = 0

while eggs_size and papers_size:
    current_egg = eggs_size[0]

    if current_egg <= 0:
        eggs_size.popleft()
        continue

    if current_egg == 13:
        eggs_size.popleft()
        papers_size[0], papers_size[-1] = papers_size[-1], papers_size[0]
        continue

    current_paper = papers_size[-1]

    if current_paper + current_egg <= BOX_SIZE:
        boxes_count += 1

    eggs_size.popleft()
    papers_size.pop()

if boxes_count > 0:
    print(f'Great! You filled {boxes_count} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_size)}")
if papers_size:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers_size)}")

