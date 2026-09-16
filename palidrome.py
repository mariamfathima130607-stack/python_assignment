#Check for palindrome

text = input("enter any word:") 
if text == text[::-1]:
 print("Palindrome")
else:
 print("Not a Palindrome")
