def negs_vs_positives(*args):
    negative_nums = 0
    positive_nums = 0

    for num in args:
        if num < 0:
            negative_nums += num
        else:
            positive_nums += num

    return negative_nums, positive_nums


nums = [int(x) for x in input().split()]
negative, positive = negs_vs_positives(*nums)

print(negative)
print(positive)

if abs(negative) > positive:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
