# EXERCISE 7 

wt=int(input("Enter your weight in kilograms= "))
ht=float(input("Enter your height in meters= "))
BMI=int(wt/ht**2)
if(BMI<18.5):
    print(f"Your BMI is {BMI} and you are Underweight")
elif(BMI>18.5 and BMI<24.9):
    print(f"Your BMI is {BMI} and you are Normal weight")
elif(BMI>24.9 and BMI<29.9):
    print(f"Your BMI is {BMI} and you are Overweight")
elif(BMI>=30):
    print(f"Your BMI is {BMI} and you are Obese")
else:
    print("Invalid Input")   