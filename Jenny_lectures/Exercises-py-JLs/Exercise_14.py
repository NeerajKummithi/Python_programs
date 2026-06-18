#EXERCISE 14 - PROGRAM TO CALCULATE AVERAGE HEIGHT FROM A LIST OF HEIGHTS.

# use input() , for loop, split() , range()
#  don't use sum() , len()
# and the result should be rounded to whole number.

heights=input("Enter the heights with spaces: ").split()
total=0
n=0
print(heights)
for height in heights:
    total+=int(height)
    n+=1
avg_height=round(total/n)    
print(f"The avg_height of the heights is {avg_height} ")            
