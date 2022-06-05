from collections import deque

bowls_ramen_stack = [int(x) for x in input().split(', ')]
customers_q = deque([int(x) for x in input().split(', ')])

while bowls_ramen_stack and customers_q:
    current_ramen = bowls_ramen_stack[-1]
    current_customer = customers_q[0]

    if current_ramen == current_customer:
        bowls_ramen_stack.pop()
        customers_q.popleft()

    elif current_ramen > current_customer:
        bowls_ramen_stack[-1] -= current_customer
        customers_q.popleft()

    elif current_customer > current_ramen:
        customers_q[0] -= current_ramen
        bowls_ramen_stack.pop()

if not customers_q:
    print('Great job! You served all the customers.')
    if bowls_ramen_stack:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_ramen_stack)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers_q)}")





