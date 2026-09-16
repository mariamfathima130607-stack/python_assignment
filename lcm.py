a=int(input("enter any number:"))
b=int(input("enter any number:"))
def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x
lcm =(a	*b)//gcd(a,b)
print(lcm)
