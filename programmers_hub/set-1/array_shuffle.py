# 7.SHUFFLE AN ARRAY
# Given a range of numbers print the numbers such that they are shuffled.
import random

array=[]
s=int(input("enter the starting number: "))
e=int(input("enter the ending number: "))
for i in range(s,e):
    array.append(i)
random.shuffle(array)
print(array)    


#if any of the given ranges are same, the orders of the numbers must vary.


array=[]
s=int(input("enter the starting number: "))
e=int(input("enter the ending number: "))
n=int(input("Enter how many shuffles: "))
for i in range(s,e):
    array.append(i)
for j in range(n):
    random.shuffle(array)
    print(array)   