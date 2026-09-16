#Count Positive, Negative, and Zero Values in a List

numbers = [4, -2, 0, 7, -5, 0, 3]
positive = negative = zero = 0
for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
