milk = 1000
coffee = 200
water = 500

def cappuccino():
    global milk, coffee, water
    if milk < 150 or coffee < 15 or water < 35:
        return False
    milk -= 150
    coffee -= 15
    water -= 35
    return True

def espresso():
    global coffee, water
    if coffee < 15 or water < 35:
        return False
    coffee -= 15
    water -= 35
    return True

def latte():
    global milk, coffee, water
    if milk < 250 or coffee < 15 or water < 35:
        return False
    milk -= 250
    coffee -= 15
    water -= 35
    return True