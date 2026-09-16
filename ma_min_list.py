#finad max and min in list
numbers	=[12,45,2,41,31,10,8]
largest	=smallest=numbers[0]
for num in numbers:
    if  num	>largest:
        largest	=num
    if  num	<smallest:
        smallest=num
print("Largest:",largest)
print("Smallest:",smallest)
