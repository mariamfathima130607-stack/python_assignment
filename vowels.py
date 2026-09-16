#count vowels
text=input("enter a string:").lower()
vowels="aeiou"
count=0
for char in text:
    if char in vowels:
    	count+= 1
print(count)
