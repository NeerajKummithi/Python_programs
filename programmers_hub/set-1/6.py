# 6.CRICKET SCORES
# Given a timeline of scores, find the individual scores of player 1 and player 2 and extras
# W-Wide  N-No Ball .-Dot Ball
# Consider the game starts from player1

scores=input("Enter the scores").split( )
p1=p2=extras=0
count=0
for i in range(len(scores)):
    if count<=5:
        if scores[i]  not in ['w','W','n','N']:
          if scores[i] in ['.']:
              count+=1
              scores[i]=0
          else:    
            count+=1
            scores[i]=int(scores[i])
            p1+=scores[i]
        else:
            extras+=1
            p1+=1 
    elif count<12:
        if scores[i]  not in ['w','W','n','N']:
            if scores[i] in ['.']:
              count+=1
              scores[i]=0
            else:  
                count+=1
                scores[i]=int(scores[i])
                p2+=scores[i]
        else:
            extras+=1
            p2+=1
print(f"P1={p1} \n P2={p2} \n Extras={extras}")    

