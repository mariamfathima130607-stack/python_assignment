#Factorial of a number

num = int(input("enter any number:"))
fact = 1
for i in range(1, num + 1):
    fact*= i
print(fact)


