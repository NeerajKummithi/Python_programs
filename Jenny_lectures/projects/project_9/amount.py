
cash=0
c_total=0

def amount_cal():
    global c_total
    print("Insert the money")
    c_5=int(input("No. of 5rs coins: "))
    c_10=int(input("No. of 10rs coins: "))
    c_20=int(input("No. of 20rs coins: "))
    c_total=c_5*5+c_10*10+c_20*20
