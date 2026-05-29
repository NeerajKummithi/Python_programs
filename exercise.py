
#EXERCISE 4 - BMI
# wt=int(input("Enter your weight in kilograms= "))
# ht=float(input("Enter your height in meters= "))
# BMI=int(wt/ht**2)
# print("Your BMI is: ",BMI)

# ==========================================================================================================================================================
#EXERCISE 5
# age=int(input("enter your age= "))
# a=(100-age)*365
# b=(100-age)*52
# c=(100-age)*12
# print(f"You have {a} days , {b} weeks ,{c} months left")
# ==========================================================================================================================================================

#EXERCISE 6 - (Check whether given number is even or odd)
# x=int(input("Enetr a number= "))
# if(x%2==0):
#     print("x is even")
# else:
#     print("x is odd")    
# ==========================================================================================================================================================

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
# ==========================================================================================================================================================

# EXERCISE 8 -(whether given year is leap year or not)
# year=int(input("Enter the year= "))
# if(year%4==0 and year%100!=0 )or( year%400==0):
#     print(f"{year} is a Leap year")
# else:
#     print(f"{year} is  not a Leap year")    
# ==========================================================================================================================================================
   
#EXERCISE 9 -(Pizza order program)
# order=int(input("Select your pizza \n Pizza Type \t\t Cost in Rs. \n 1.Small pizza  \t 100 \n 2.Medium pizza \t 200 \n 3.Large pizza  \t 300 \n choice= "))
# bill=0

# if(order==1):
#     bill+=100
#     print("You have ordered Small Pizza ")
    
# elif(order==2):
#     bill+=200
#     print("You have ordered Medium Pizza")
    
    
# elif(order==3):
#     bill+=300
#     print("You have ordered Large Pizza")

# else:
#      print("You have not ordered anything")
   

# choice=input("You want pepperoni or not?(y/n)")
# if(choice=='y' or choice=='Y'):
#     print("You have added pepperoni")
#     if(order==1):
#         bill+=30
#     else:
#          bill+=50    

# cheese=input("Do you want extra cheese? (y/n)") 
# if(cheese=='y' or cheese=='Y'):    
#     bill+=50
#     print("You added extra cheese")

# print(f"Your total bill is Rs.{bill}")

# print("Thank You 🙏 Visit Again")                              
# ==========================================================================================================================================================

#EXERCISE 10 - (LOVE CALCULATOR)

# B=input("Enter the boy name = ")
# G=input("Enter the girl name = ")

# b=B.lower()
# g=G.lower()

# T=b.count("t")+g.count("t")
# R=b.count("r")+g.count("r")
# U=b.count("u")+g.count("u")
# E1=b.count("e")+g.count("e")
# L=b.count("l")+g.count("l")
# O=b.count("o")+g.count("o")
# V=b.count("v")+g.count("v")
# E2=b.count("e")+g.count("e")

# true=T+R+U+E1
# love=L+O+V+E2

# print(f"Percentage of love between {B} and {G} is {true}{love}%")
# ==========================================================================================================================================================




