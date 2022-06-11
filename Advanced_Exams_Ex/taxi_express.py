from collections import deque

customers_q = deque([int(x) for x in input().split(', ')])
taxis_stack = [int(x) for x in input().split(', ')]

customers_total_time = sum(customers_q)

while customers_q and taxis_stack:
    current_customer = customers_q[0]
    current_taxi = taxis_stack[-1]

    if current_taxi >= current_customer:
        customers_q.popleft()
        taxis_stack.pop()
    else:
        taxis_stack.pop()

if customers_q:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(x) for x in customers_q])}')
else:
    print('All customers were driven to their destinations')
    print(f'Total time: {customers_total_time} minutes')


