#2.PASSWORD STRENGTH
#find the strength of the given password string based on the conditions.
#four rules were given based on the type and no.of characters in the string.
# WEAK-only rule 1 is satisfied or rule 1 is not satisfied
# MEDIUM-two rules are satisfied
# GOOD-three rules satisfied
# STRONG-all four rules satisfied
#{Let the rules be
# 1.atleast one uppercase letter
# 2.atleast one lowercase letter
# 3.atleast one digit (0-9)
# 4.atleast one spacial character(!,@,#,$,%,^,&,*,?)}

password=input("Enter ypur password: ")
count=upper=lower=digit=special=0
for i in password:
    if i.isupper()==True:
        upper=1
    if i.islower()==True:
        lower=1
    if i.isdigit()==True:
        digit=1
    if i.isalnum()==False:
        special=1

count=upper+lower+digit+special        
if count==1 or count==0:
    print("WEAK")                 
if count==2:
    print("MEDIUM")                 
if count==3:
    print("GOOD")                 
if count==4:
    print("STRONG")                 
