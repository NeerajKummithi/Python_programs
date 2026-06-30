import menu
import coffee_list
import amount


while True:
    order=input("What you would like to have(Cappucino/Expresso/Latte)?").lower()

    #cappuccino
    if order == 'cappuccino':
        amount.amount_cal()
        if amount.c_total >= 125:
            if coffee_list.cappuccino():
                change = amount.c_total - 125
                amount.cash += 125
                if change > 0:
                    print(f"Your change is {change}")
                print("Here's your Cappuccino! ☕")
            else:
                print("Sorry, out of stock for that.")
                amount.cash-=125
        else:
            print("Amount is not enough!")

    #latte
    elif order == 'latte':
        amount.amount_cal()
        if amount.c_total >= 140:
            if coffee_list.latte():
                change = amount.c_total - 140
                amount.cash += 140
                if change > 0:
                    print(f"Your change is {change}")
                print("Here's your Latte! ☕")
            else:
                print("Sorry, out of stock for that.")
                amount.cash-=140
        else:
            print("Amount is not enough!") 

    #expresso         
    elif order == 'expresso':
        amount.amount_cal()
        if amount.c_total >= 90:
            if coffee_list.espresso():
                change = amount.c_total - 90
                amount.cash += 90
                if change > 0:
                    print(f"Your change is {change}")
                print("Here's your Espresso! ☕")
            else:
                print("Sorry, out of stock for that.")
                amount.cash-=90
        else:
            print("Amount is not enough!")

    #report
    elif order == 'report':
        print(f"Milk-left: {coffee_list.milk}")
        print(f"Coffee-left: {coffee_list.coffee}")
        print(f"Water-left: {coffee_list.water}")
        print(f"Total-sales: {amount.cash}")

    #off the machine         
    elif order=='off':
        print("The coffee machine is closed!")
        break
    else:
        print("Sorry not on the menu.Thanks for coming.")


