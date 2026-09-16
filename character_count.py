#character count
text=input("enter a string:")
counts={}
for char in text:
    if char in counts:
        counts[char]+=1
    else:
        counts[char]=1
for char,count in counts.items():
    print(f"{char}:{count}")
