#Fibonacci  series

n = int(input("enter any number:"))
a, b = 0, 1
for _ in range(n):
    print(a,end="\t")
    a, b = b, a + b

