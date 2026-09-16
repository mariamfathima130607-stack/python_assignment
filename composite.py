#Check for composite number
num = int(input("enter any number:"))
is_composite = False
if num > 1:
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            is_composite = True
            break
print("Composite" if is_composite else "Not Composite")
