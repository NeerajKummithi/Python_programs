#EXERCISE 15 - PROGRAM TO FIND MAXIMUM NUMBER OF THE LIST OF NUMBERS

numbers=input("Enter the numbers: ").split()
max=numbers[0]
for num in numbers:
    if num>max:
        max=num
print(f"Maximum number of the list is {max}")        