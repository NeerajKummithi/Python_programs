#PASSWORD GENERATOR

#the output should be like this:
#Welcome to Password Generator!
#How many characters would you like in a password?
#How many letters would you like in password?
#How many symbols you like?
#HOW many digits would you like?

import random
import string

print("Welcome to Password Generator!")
cn=input("How many characters would you like in a password?")
ln=int(input("How many letters would you like in password?"))
sn=int(input("How many symbols you like?"))
dn=int(input("HOW many digits would you like?"))

pwd=[]

for i in range(ln):
    pwd.append(random.choice(string.ascii_letters))

for j in range(sn):
    pwd.append(random.choice(string.punctuation))

for k in range(dn):
    pwd.append(str(random.randint(0,9)))


random.shuffle(pwd)
password=''
for l in pwd:
    password+=l
print(password)    

