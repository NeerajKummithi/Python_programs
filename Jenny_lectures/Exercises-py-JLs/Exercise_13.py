# EXERCISE 13
# storing money in a selected locker 

x=int(input('Enter the amount to be stored: '))
list1=[1,1,1]
list2=[1,1,1]
list3=[1,1,1]
final_list=[list1,list2,list3]
n=input("Enter the locker number: ").split( )
r=int(n[0])
c=int(n[1])
final_list[r][c]=x
print(final_list)