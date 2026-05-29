
#EXERCISE 4 - BMI
# wt=int(input("Enter your weight in kilograms= "))
# ht=float(input("Enter your height in meters= "))
# BMI=int(wt/ht**2)
# print("Your BMI is: ",BMI)

#EXERCISE 5
# age=int(input("enter your age= "))
# a=(100-age)*365
# b=(100-age)*52
# c=(100-age)*12
# print(f"You have {a} days , {b} weeks ,{c} months left")

#EXERCISE 6 - (Check whether given number is even or odd)
# x=int(input("Enetr a number= "))
# if(x%2==0):
#     print("x is even")
# else:
#     print("x is odd")    

#EXERCISE 7 
# wt=int(input("Enter your weight in kilograms= "))
# ht=float(input("Enter your height in meters= "))
# BMI=int(wt/ht**2)
# if(BMI<18.5):
#     print(f"Your BMI is {BMI} and you are Underweight")
# elif(BMI>18.5 and BMI<24.9):
#     print(f"Your BMI is {BMI} and you are Normal weight")
# elif(BMI>24.9 and BMI<29.9):
#     print(f"Your BMI is {BMI} and you are Overweight")
# elif(BMI>=30):
#     print(f"Your BMI is {BMI} and you are Obese")
# else:
#     print("Invalid Input")   
# 
# EXERCISE 8 -(whether given year is leap year or not)
# year=int(input("Enter the year= "))
# if(year%4==0 and year%100!=0 )or( year%400==0):
#     print(f"{year} is a Leap year")
# else:
#     print(f"{year} is  not a Leap year")    
         
#EXERCISE 9 -(Pizza order program)
order=int(input("Enter your choice from \n 1.Small pizza \n 2.Medium pizza \n 3.Large pizza \n choice= "))
bill=0

if(order==1):
    bill=100
    print("You have ordered Small Pizza ")
    choice=input("You want pepperoni or not?(y/n)")
    if(order==1 and (choice=='y' or choice=='Y')):
        bill=bill+30
        print("You have added pepperoni")
    cheese=input("Do you want extra cheese? (y/n)") 
    if(cheese=='y' or cheese=='Y'):
                print(f"Your total bill is {bill+50}")
elif(order==2):
    bill=200
    print("You have ordered Medium Pizza")
    choice=input("You want pepperoni or not?(y/n)")
    if(order ==2 and (choice=='y' or choice=='Y')):
        bill=bill+50
        print(f"You have added pepperoni") 
    cheese=input("Do you want extra cheese? (y/n)") 
    if(cheese=='y' or cheese=='Y'):
            print(f"Your total bill is {bill+50}")
elif(order==3):
    bill=300
    print("You have ordered Large Pizza")
    choice=input("You want pepperoni or not?(y/n)")
    if( order==3 and (choice=='y' or choice=='Y')):
        bill=bill+50
        print(f"You have added pepperoni") 
    cheese=input("Do you want extra cheese? (y/n)") 
    if(cheese=='y' or cheese=='Y'):
            print(f"Your total bill is {bill+50}")
else:
    print("no order placed")
print("Enjoy Your Pizza")                              