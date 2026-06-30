# def fun_name():
#     function body
#     return expression

# def greet():
#     print("Hi Neeraj")
#     print("Good Morning")

# greet()    

# =================================================================
# Functions with arguements

# def fun_name(parameters):
#     function body
#     return expression
#fun_name(arguements)

# def greet(name):
#     print(f"Hi {name}")
#     print("Good Morning")

# greet('Neeraj')
# greet('Stuart')    

#================================================================
#Types of Arguements

# def greet(name,dept):
#     print(f"Hi {name}")
#     print(f"Welcome to {dept} department")

# greet("Neeraj","CSE") #Default arguements
# """Hi Neeraj
# Welcome to CSE department"""
# greet("CSE","Neeraj") #positional arguements - position decides the value of parameters
# """Hi CSE
# Welcome to Neeraj department"""
# greet(dept="CSE",name="Neeraj") #Keyword arguements - keyword name decides value  
# """Hi Neeraj
# Welcome to CSE department"""

# ======================================================================
# def add(*numbers):             #
#     sum=0
#     for c in numbers:
#         sum+=c
#     print(sum)
# add(2,5,222,3)    

#=======================================================================
# *args and **kwargs

# def add(*numbers):                    #*args
#      sum=0
#      for c in numbers:
#         sum+=c
#      print(sum)
# add(2,5,22,3)

# def info(**info1):                   #**kwargs
#     name=info1['name']
#     age=info1['age']
#     city=info1['city']
#     print(f"My name is {name} , {age} years old and living in {city}")

# info(name="Neeraj",age=20,city="Anantapuram")

#=====================================================================

# functions with return statement 

# def add(a,b):
#     return a+b
# result=add(5,5)
# print(result)    

#=====================================================================

#functions with multiple return values

# import statistics

# def mean_mode_median(list1):
#     return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)

# a,b,c=mean_mode_median([56,54,92,15,36,25])
# print(f"Mean is {a} , Median is {b} , Mode is {c}")    