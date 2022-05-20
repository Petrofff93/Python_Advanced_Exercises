students_count = int(input())
students_dict = dict()

for _ in range(students_count):
    student, grade = input().split()
    if student not in students_dict:
        students_dict[student] = [float(grade)]
    else:
        students_dict[student] += [float(grade)]

for k, v in students_dict.items():
    print(f"{k} -> {' '.join([str('{:.2f}'.format(x)) for x in v])}", f"(avg: {sum(v)/len(v):.2f})")
    