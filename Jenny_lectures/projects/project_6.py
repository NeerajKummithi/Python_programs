#CALCULATOR PROGRAM

def calculate(fn, op, sn):
    if op == "+":
        return fn + sn
    elif op == "-":
        return fn - sn
    elif op == "*":
        return fn * sn
    elif op == "/":
        if sn == 0:
            print("Cannot divide by zero!")
            return fn
        return fn / sn
    else:
        print("Invalid operation!")
        return fn


result = None

while True:

    # New calculation
    if result is None:
        fn = float(input("Enter the first number: "))
        op = input("Pick an operation (+, -, *, /): ")
        sn = float(input("Enter the second number: "))
        result = calculate(fn, op, sn)
        print("Result =", result)

    # Menu
    choice = input("\nEnter y (continue), n (new calculation), x (exit): ").lower()

    if choice == "y":
        op = input("Pick an operation (+, -, *, /): ")
        sn = float(input("Enter the second number: "))
        result = calculate(result, op, sn)
        print("Result =", result)

    elif choice == "n":
        result = None      # Starts a new calculation

    elif choice == "x":
        print("Calculator Closed.")
        break

    else:
        print("Invalid choice!")
    
    
