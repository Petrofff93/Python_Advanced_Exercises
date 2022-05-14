from collections import deque

kids_q = deque(input().split())
n = int(input())

while len(kids_q) > 1:
    kids_q.rotate(-n)
    print(f"Removed {kids_q.pop()}")

print(f"Last is {kids_q[0]}")


