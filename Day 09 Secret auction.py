# FREE SECRET AUCTION Program
#makes use of dictionaries 
#DAY -09 Program  instructed by Dr. Angela Yu

#imported the logo from another python file and printed
from bidding_ascii import art
print(art)


def clear_screen_spyder(num_lines=100):
    """Clears the Spyder Console by printing empty lines. Parameters:
       num_lines (int): Number of empty lines to print. Default is 100."""
    print("\n" * num_lines)

def max_bid(bid_dictionary, name, bid_amount):
    max_bid_value = 0
    for name in bid_dictionary:
        value = int(bid_dictionary[name])
        if value > max_bid_value:
            max_bid_value = 0
            max_bid_value += value
    print(f"The Winner of the Secret Auction bid is {name} \nfor bidding the amount of {max_bid_value}")

def add_value(bid_dictionary, name, bid_amount):
    bid_dictionary[name] = bid_amount
    
bid_dictionary = {}   #empty dictionary to store the bidder's name and bid
loop = True
while loop:
    print("Welcome to Secret Bidding Program!")
    name = input("What is your name: ")
    bid_amount = int(input("What's your bid: $"))
    
    add_value(bid_dictionary, name, bid_amount)
    
    ans = input("Are there any other bidders ?? Type y / n: ")
    if ans == 'y':
        clear_screen_spyder(num_lines = 100)
        loop = True
    else: 
        max_bid(bid_dictionary, name, bid_amount)
        #print(bid_dictionary)
        loop = False
        print("------------------------------")
        
        
    