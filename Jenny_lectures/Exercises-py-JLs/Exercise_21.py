#Paint Coverage

import math

def coverage(**paint):
    # h=int(input("Enter the height of the wall: "))
    # w=int(input("Enter the width of the wall: "))
    h=paint['h']
    w=paint['w']
    a=h*w
    cover=math.ceil(a/7)
    print(f"The are of the wall is {a} sq.m and it requires {cover} cans of paint.")

coverage(h=15,w=15)