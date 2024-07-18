"""\ Python Pizza order program"""

print("--Welcome to Python Pizza Corner---")

size = input("What size pizza you wish to have [s /m /l]: ")
add_peporoni = input("Do you wanna add some peporoni [y/n]: ")
add_cheese = input("Some extra cheese[y/n]: ")
bill = 0

if size == "s":
    bill = 15
    print("Your small size pizza costs $15")
elif size == "m":
    bill = 20
    print("Your medium size pizza costs $20")
elif size == "l":
    bill = 25
    print("Your large size pizza costs $25") 
else:
    print("Please choose an appropriate size.")
    
if add_peporoni == "y":
    if size == "s":
        bill +=2
    
    if size == "m" or size == "l":
        bill +=3

if add_cheese == "y":
    bill +=1
    
print(f"Your total bill has come upto ${bill}. \nThank you for coming to Python Pizza! Have a great time!")