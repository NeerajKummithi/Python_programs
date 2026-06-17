# EXERCISE 9 -(Pizza order program)

order=int(input("Select your pizza \n Pizza Type \t\t Cost in Rs. \n 1.Small pizza  \t 100 \n 2.Medium pizza \t 200 \n 3.Large pizza  \t 300 \n choice= "))
bill=0

if(order==1):
    bill+=100
    print("You have ordered Small Pizza ")
    
elif(order==2):
    bill+=200
    print("You have ordered Medium Pizza")
    
    
elif(order==3):
    bill+=300
    print("You have ordered Large Pizza")

else:
     print("You have not ordered anything")
   

choice=input("You want pepperoni or not?(y/n)")
if(choice=='y' or choice=='Y'):
    print("You have added pepperoni")
    if(order==1):
        bill+=30
    else:
         bill+=50    

cheese=input("Do you want extra cheese? (y/n)") 
if(cheese=='y' or cheese=='Y'):    
    bill+=50
    print("You added extra cheese")

print(f"Your total bill is Rs.{bill}")

print("Thank You 🙏 Visit Again")                              