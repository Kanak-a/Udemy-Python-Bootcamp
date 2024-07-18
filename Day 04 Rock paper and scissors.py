#ICONIC ROCK - PAPER - SCISSORS 
#RPS Game
#random generated opponent -> Computer
import random
rock = """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
"""
paper = """
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)

"""
scissors = """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)

"""

loop = True
while(loop) :
    print("What do you choose: ")
    choice = input("Type 0 for Rock, 1 for paper and 2 for scissors: ")
    if choice == "0":
        print("Rock")
        print(rock)
        
    elif choice == "1":
        print("Paper")
        print(paper)
        
    elif choice == "2":
        print("Scissors")
        print(scissors)
     
    
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Rock")
        print(rock)
        
    elif computer_choice == 1:
        print("Paper")
        print(paper)
        
    elif computer_choice == 2:
        print("Scissors")
        print(scissors)  
        
        
        
    print("\n")
        

    if int(choice) ==0:
        if computer_choice == 0:
            print("It's a tie")
        elif computer_choice == 1:
            print("Computer wins")
        else:
            print("You win!")
    
    if int(choice) == 1:
        if computer_choice == 0:
            print("You win")
        elif computer_choice == 1:
            print("It's a tie")
        else:
            print("Computer wins")
        
    if int(choice) == 2:
        if computer_choice == 0:
            print("Computer wins")
            
        elif computer_choice == 1:
            print("You win!")
        else:
            print("It's a tie!")
    
    ans = input("Do you wish to continue: [y/n] ")
    if ans == "y" :
        continue
    else:
        loop = False
    print("\n Thankyou for playing Rock Paper and Scissors.\nHope you enjoyed!")   
        
        