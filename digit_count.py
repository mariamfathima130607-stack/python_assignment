#number of digits count
num =int(input("enter any number:"))
count=0
if num==0:
    count=1
else:
    num	=abs(num)
while num>0:
    count+=1
    num//=10
print(count)
