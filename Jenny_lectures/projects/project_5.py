#SILENT AUCTION PROGRAM

import os

def bids():
        name=input("What is your name?: ")
        bid=int(input("What is your bid?: "))
        new_bid={}
        new_bid['name']=name
        new_bid['bid']=bid
        bids_set.append(new_bid)
        
def compare_bids():
    winner = bids_set[0]
    for entry in bids_set:
        if entry['bid'] > winner['bid']:
            winner = entry
    print(f"\nThe winner is {winner['name']} with a bid of ${winner['bid']}!")

bids_set=[] 

while True:
    bids()
    choice=input("Are there any other bids?(y/n)")
    if choice=='n':
        compare_bids()
        break
    os.system('cls' if os.name == 'nt' else 'clear')

