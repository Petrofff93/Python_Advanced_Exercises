first_seq = set([int(x) for x in input().split()])
second_seq = set([int(x) for x in input().split()])

commands = int(input())

for _ in range(commands):
    expression = input().split()

    if f"{expression[0]} {expression[1]}" == 'Add First':
        for el in expression:
            if el.isdigit():
                first_seq.add(int(el))

    elif f"{expression[0]} {expression[1]}" == 'Add Second':
        for el in expression:
            if el.isdigit():
                second_seq.add(int(el))

    elif f"{expression[0]} {expression[1]}" == 'Remove First':
        for el in expression:
            if el.isdigit():
                if int(el) in first_seq:
                    first_seq.remove(int(el))

    elif f"{expression[0]} {expression[1]}" == 'Remove Second':
        for el in expression:
            if el.isdigit():
                if int(el) in second_seq:
                    second_seq.remove(int(el))

    elif f"{expression[0]} {expression[1]}" == 'Check Subset':
        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print('True')
        else:
            print('False')

first_seq = sorted([x for x in first_seq])
second_seq = sorted([x for x in second_seq])

print(*first_seq, sep=', ')
print(*second_seq, sep=', ')
