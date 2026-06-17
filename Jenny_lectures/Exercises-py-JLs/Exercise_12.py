# EXERCISE 12 
# WRITE A PROGRAM WHICH SELECT A RANDOM NAME FROM A LIST OF NAMES & THE PERSON SELECTED WILL HAVE TO PAY FOR EVERYBODY'S FOOD BILL.

import random  

names=list(input("Enter your names with commas: ").split(","))
# print(random.choice(names))
n=len(names)
result=random.randrange(0,n)
print(names[result])