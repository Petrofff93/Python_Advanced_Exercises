expression = input()
opening_b = []
balanced = True

for ch in expression:
    if ch in '([{':
        opening_b.append(ch)
    elif not opening_b:
        balanced = False
        break
    else:
        last_opening = opening_b.pop()
        if f'{last_opening}{ch}' not in '(){}[]':
            balanced = False
            break
if ')' not in expression and '}' not in expression and ']' not in expression:
    balanced = False

if balanced:
    print('YES')
else:
    print('NO')


