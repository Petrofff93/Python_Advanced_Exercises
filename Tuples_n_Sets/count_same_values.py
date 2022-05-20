numbers = [float(x) for x in input().split()]
num_dict = dict()

for num in numbers:
    if num not in num_dict:
        num_dict[num] = 0
    num_dict[num] += 1

for k, v in num_dict.items():
    print(f"{k} - {v} times")
    