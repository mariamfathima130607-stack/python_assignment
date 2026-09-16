numbers	=[12,45,2,41,31,10,8]
largest=second_largest=float('-inf')
for num in numbers:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and	num!=largest:
        second_largest=num
print(second_largest)
