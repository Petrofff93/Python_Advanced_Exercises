expression = input()
my_dict = dict()

for el in expression:
    if el not in my_dict:
        my_dict[el] = 0
    my_dict[el] += 1

for k, v in sorted(my_dict.items()):
    print(f"{k}: {v} time/s")
    