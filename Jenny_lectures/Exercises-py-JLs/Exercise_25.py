# COunting no. of days in a selected month

def leap_check(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_month(year,month):
    if month==1:
        print(f"{year} year January month has 31 days")
    if month==2:
        leap_state = leap_check(year)
        if leap_state:
            print(f"{year} year February month has 29 days")
        else:
            print(f"{year} year February month has 28 days")
    if month==3:
        print(f"{year} year March month has 31 days")
    if month==4:
        print(f"{year} year April month has 30 days")
    if month==5:
        print(f"{year} year May month has 31 days")
    if month==6:
        print(f"{year} year June month has 30 days")
    if month==7:
        print(f"{year} year July month has 31 days")
    if month==8:
        print(f"{year} year August month has 31 days")
    if month==9:
        print(f"{year} year September month has 30 days")
    if month==10:
        print(f"{year} year October month has 31 days")
    if month==11:
        print(f"{year} year November month has 30 days")
    if month==12:
        print(f"{year} year December month has 31 days")

year=int(input("emter the year: "))
month=int(input("emter the month number: "))

days_in_month(year,month)       