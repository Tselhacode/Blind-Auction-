from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")


def highest_bidder(bidders):
  max_bid = 0
  winner = ""
  for bidder in bidders:
    if bidders[bidder] > max_bid:
      max_bid = bidders[bidder]
      winner = bidder
  print(f"The winner is {winner} with the bid amount of {max_bid}")

dicti = {}
bidding_finished = False
while not bidding_finished:
  name = input("What is your name?:")
  bid = int(input("what is your bid?: $"))
  dicti[name] = bid
  yes_no = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if yes_no == 'no':
    bidding_finished = True
    highest_bidder(dicti)
  elif yes_no == 'yes':
    clear()







