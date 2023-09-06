from sys import exit
from art import logo

continue_bid = True
bid_dict = {}
print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for name in bidding_record:
        bid_amount = bidding_record[name]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
        

while continue_bid:
    bidder = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    next_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")
    bid_dict[bidder] = bid

    if next_bidder == "yes":
        exit()
    
    elif next_bidder == "no":
        continue_bid = False
        find_highest_bidder(bid_dict)
        
