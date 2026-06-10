

#5.MATRIX ADDITION
#Given n integer arrays of different size, find the addition of numbers represented by the arrays.

all_arrays=[]
all_num=[]
total_sum=0
n1=int(input("Enter the no. of arrays: "))
for i in range(n1):
    n2=int(input("Enter the size of the array: "))
    arr=[]
    for j in range(n2):
        x=input()
        arr.append(x)
    all_arrays.append(arr)        
for i in all_arrays:
    num=""
    for j in i:
        num+=j
    all_num.append(int(num))
for i in all_num:
    total_sum+=i
print(all_num)    
print(total_sum)    

            
