from collections import deque

expression = input().split()
result = 0
current_nums = deque()
current_nums2 = deque()


for item in expression:
    if item.isdigit():
        current_nums.append(int(item))
    elif len(item) > 1 and item[0] == '-':
        current_nums.append(int(item))
    else:
        if result == 0 and not current_nums2:
            result = current_nums.popleft()
        else:
            result = current_nums2.popleft()
        while current_nums:
            if item == "+":
                result += current_nums.popleft()
            elif item == "-":
                result -= current_nums.popleft()
            elif item == "*":
                result *= current_nums.popleft()
            elif item == "/":
                result //= current_nums.popleft()
        current_nums2.append(result)

print(result)
