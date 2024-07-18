#Day-02 project -
'''To build a tip calculator'''

print("Welcome to tip calculator!")
bill = float(input("Your total bill : $"))
tip = int(input("How much tip you wish to pay [10/12/15 %] : "))
total_tip = (tip/100) * bill
people = int(input("How many people to split the bill? : "))

split_bill = bill/people
split_tip = total_tip/people


total = round(split_bill +split_tip, 2)
print(f"Each person must pay : ${total}")