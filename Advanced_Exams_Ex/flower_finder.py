from collections import deque

flowers_collection = {'rose', 'tulip', 'lotus', 'daffodil'}
letters_found = []

vowels = deque([x for x in input().split()])
consonants = [x for x in input().split()]
is_found = True

while vowels and consonants:
    if len(flowers_collection) < 4:
        break

    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    letters_found.append(current_consonant)
    letters_found.append(current_vowel)

    for flower in flowers_collection:
        for ch in flower:
            if ch not in letters_found:
                is_found = False
        if is_found:
            print(f'Word found: {flower}')
            flowers_collection.remove(flower)
            break
        is_found = True


if is_found and len(flowers_collection) != 4:
    if vowels:
        print(f'Vowels left: {" ".join(vowels)}')
    if consonants:
        print(f'Consonants left: {" ".join(consonants)}')
else:
    if len(flowers_collection) == 4:
        print('Cannot find any word!')
    if vowels:
        print(f'Vowels left: {" ".join(vowels)}')
    if consonants:
        print(f'Consonants left: {" ".join(consonants)}')



