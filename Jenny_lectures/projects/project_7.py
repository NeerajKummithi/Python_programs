import random

print("I will select a number from 1 to 50")
#number=random.randint(1,50)
number=45
level=input("choose level of difficulty 'easy' or 'hard' : ").lower()
if level=='easy':
    n=10
    print("you have 10 chances to guess the mumber")
elif level=='hard':
    n=5
    print("you have 5 chances to guess the mumber")    
while n>1:
    guess=int(input("Enter your guess: "))
    if guess<number:
        print("The guessed number is too low")
    elif guess>number:
        print("The guessed number is too high")
    elif guess==number:
        print(f"The guessed number {guess} is correct")
        break
    else:
        print("invalid ")
    n=n-1
    print(f"You have {n} chances left.Guess the number correctly")
else:
    print("You have no chances left.You had lost")
