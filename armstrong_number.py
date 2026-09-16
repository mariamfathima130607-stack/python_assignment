#armstrong number
num = int(input("enter any number:")) 
num_str = str(num) 
power = len(num_str)
total = sum(int(digit) ** power for digit in num_str)
print("Armstrong" if total == num else "Not Armstrong")
