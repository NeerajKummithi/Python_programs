#3.FIRST OCCURENCES
#Given two strings, find the first occurence of all characters of second string in the first string and print the characters between the least and highest index.   

STR1=input("Enter your first string: ")
STR2=input("Enter your second string: ")
str1=STR1.lower()
str2=STR2.lower()

list=[]
for i in str2:
        list.append(str1.find(i))
while -1 in list:
    list.remove(-1)
print(STR1[min(list):max(list)+1])    