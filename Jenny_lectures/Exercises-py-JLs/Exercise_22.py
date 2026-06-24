#Prime Checker

def is_prime():
    if(n%2==0 or n%3==0 or n%5==0 or n%7==0):
        print(f"{n} is not a prime numbrer.")
    else:
        print(f"{n} is a prime number") 

n=int(input("Enter the number to check: "))

is_prime()