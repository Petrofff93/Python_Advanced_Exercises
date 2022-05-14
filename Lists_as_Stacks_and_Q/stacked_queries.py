iterations = int(input())
empty_stack = []

for _ in range(iterations):
    command = input().split()
    if command[0] == '1':
        empty_stack.append(int(command[1]))
    elif command[0] == '2' and empty_stack:
        del empty_stack[-1]
    elif command[0] == '3' and empty_stack:
        print(max(empty_stack))
    elif command[0] == '4' and empty_stack:
        print(min(empty_stack))

if empty_stack:
    stack_to_str = [str(x) for x in reversed(empty_stack)]
    print(', '.join(stack_to_str))
