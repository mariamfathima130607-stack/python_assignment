#Sum of digits

num = int(input("enter any number:"))
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print(total)
