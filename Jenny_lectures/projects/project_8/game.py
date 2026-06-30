import logo
import database

marks=0
for i in range(len(database.data)-1):
    print("Compare")
    print(f"s1:{database.data[i]["name"]},{database.data[i]["designation"]},{database.data[i]["nationality"]}")
    print(logo.vs)
    print(f"s2:{database.data[i+1]["name"]},{database.data[i+1]["designation"]},{database.data[i+1]["nationality"]}") 
    if database.data[i]["followers"]>database.data[i+1]["followers"]:
        value='higher'
    else:
        value='lower'
    guess=input("Enter the comparision value higher or lower: ")
    if guess==value:
        print(f"Your guess is correct.")
        marks+=1        
    elif guess!=value:
        print(f"Your guess is wrong and your marks are {marks}")    
        break
    else:
        print("invalid")


    
