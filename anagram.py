#anagram
word1=input().lower().replace("	","")
word2=input().lower().replace("	","")
if  sorted(word1)==sorted(word2):
    print("Anagram")
else:
    print("Not an Anagram")
