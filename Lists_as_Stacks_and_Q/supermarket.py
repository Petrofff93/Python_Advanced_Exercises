from collections import deque

my_q = deque()
command = input()

while True:
    if command == 'Paid':
        while my_q:
            print(my_q.popleft())
    elif command == 'End':
        print(f"{len(my_q)} people remaining.")
        break
    else:
        my_q.append(command)
    command = input()

