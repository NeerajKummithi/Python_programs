# 1.PANGRAM CHECKING
# check whether all English alphabets are present in the given sentence or not.
str=input("Enter your sentence: ")
alphabet="abcdefghijklmnopqrstuvwxyz"
count=0
str1=str.lower()
for i in alphabet:
    if str1.find(i)>=0:
        count+=1
if count>=26:
    print("all letters are present.")
else:
    print("Some letters are missing.")            