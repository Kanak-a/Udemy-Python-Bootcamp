#Multiple ifs and conditional statements program
#rollercoaster ride ticket checker 

print("\nWelcomme to the rollercoaster ride's ticket counter.")
height = float(input("Enter your height in cms : "))
age = int(input("How old are you: "))
bill = 0
if height > 120:
    print("You can ride the rollercoaster! Have fun!")
    
    if age <12:
        bill = 5
        print("You'll be charged $5")
    elif age>12 and age<18:
        bill = 7
        print("You'll be charged $7")
    elif age >= 45 and age <= 55:                  #making use of logical operators
        bill = 0
    else:
        bill = 12
        print("You'll be charged &12")
    
    choice = input("You wish to take photos[y/n] : ")
    if choice == "y":
        bill +=3
    
    print(f"Your total is : {bill}")
        
    
else:
    print("Sorry, please do come once you grow taller.")
    

