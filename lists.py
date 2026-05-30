# num=[1,10,-4,4.5,56,2,3.6,7.5]
# names=["neeraj","stuart","ms"]
# mix_list=[1,"neeraj",True,9.36]

# print(num)
# print(names)
# print(mix_list)

# #index starts from 0
# print(num[1]) #positive index
# print(num[-1]) #negative index 

# print(num[1:4])  #Slicing - it takes the length not the index 
# print(num[0:6:3]) #extended slicing - the numbering means the result  starts from length 0 "first element" prints the 3rd element from that and upto 6th element
# print(num[1::2]) #the result starts from length 1 and every second element from that upto last

# num.sort() #It will sort the elements in the lists
# print(num)
# names.sort()
# print(names)
# # mix_list.sort() #TypeError: '<' not supported between instances of 'str' and 'int'

# names.reverse() #It reverses the elements in the lists
# print(names)

# num.append(96) #adds elements to the list at the end
# print(num)

# num.insert(2,87) #insert helps to add elements at particular index ,here 2 is index 
# print(num)

# num.extend([23,52,4.9]) #add muultiple elements at once at the end
# print(num)

# num[3]=53 #modifies the element at index 2
# print(num)

# num[3:6]=[53,26,15] #modifies element from index 3 to length 6 i.e, index 5
# print(num)

# num.remove(1) #removes the mentioned element from the list
# print(num)

# print(num.pop()) # if no value entered the last element is pop out
# print(num.pop(4)) # element at index 4 is popped out