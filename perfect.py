#perfect number
num =int(input())
total=0
for i in range(1,num):
    if  num %i==0:
        total+=i
print("Perfect"	if total==num else "Not	Perfect")
