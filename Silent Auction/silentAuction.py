import os
 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from silaucArt import logo

print(logo)

bids = {}
bidding_finished = False

def find_top_bidder(bidding_record):
  top_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > top_bid: 
      top_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${top_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_top_bidder(bids)
  elif should_continue == "yes":
    clear()
