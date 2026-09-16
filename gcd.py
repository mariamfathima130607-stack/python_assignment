#gcd
a=int(input("enter any number"))
b=int(input())
while b!=0:
    a,b	=b,a%b
print(a)
