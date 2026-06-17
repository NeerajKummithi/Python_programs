#ROCK, PAPER AND SCISSORS

import random 

uc=int(input(" Enter your choice: \n 1.Rock \n 2.Paper \n 3.Scissors \n "))
ccs=[1,2,3]
cc=random.choice(ccs)

if (uc==1 and cc==2) or (uc==2 and cc==3) or (uc==3 and cc==1):
    pp='Computer wins'
elif (uc==1 and cc==3) or (uc==2 and cc==1) or (uc==3 and cc==2):
    pp='User wins'
else:
    pp='It is a Draw'
if uc==1:
    uc='✊'
elif uc==2:
    uc='🖐'    
else:
    uc='✌'    
if cc==1:
    cc='✊'
elif cc==2:
    cc='🖐'    
else:
    cc='✌'    
print(f"User's choice is {uc}  and Computer's choice is {cc}  so finally {pp}")