#Love calculator
#Look out for your destiny and see with whom your compatibility is the highest!
print("Welcome to the love calculator!")
male = input("Enter the male name: ")
female = input("Enter the female name: ")
count = 0
name = male.lower()+female.lower()
total1 = name.count("t") + name.count("r") + name.count("u") + name.count("e")
total2 = name.count("l") + name.count("o") + name.count("v") + name.count("e")
score = int(str(total1 ) + str(total2) )

if score < 10 or score > 90:
    print(f"Your score is: {score} and you go together like coke and mentos.")

if score > 40 and score < 50 :
    print(f"Your score is: {score}, and you are alright together.")
    
else:
    print(f"Your score is: {score}")
