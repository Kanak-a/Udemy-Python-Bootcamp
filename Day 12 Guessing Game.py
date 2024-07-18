#Guessing the game 
import random

def GuessGame(num, level):
    if level == 'e':
        attempts = 10
    elif level == 'h':
        attempts = 5
    
    print(f"You have {attempts} remaining to guess the number.")
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == num:
            print("Thats right you guessed it! \nCongratulations on winning the game.")
            exit()
        elif guess < num:
            print("Too low. \nGuess again.")
            attempts = attempts - 1
            print(f"You have {attempts} remaining to guess the number.")
        elif guess > num:
            print("Too high. \nGuess again.")
            attempts = attempts - 1
            print(f"You have {attempts} remaining to guess the number.")
    print("You've run out of moves.")
    print("Right guess was - ", num)
    print("Uh - oh better luck next time!")



print("Welcome to the number guessing Game!")

num = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")
level = input("Choose a dificulty level. \nType 'e' for easy and 'h' for 'hard'")

GuessGame(num, level)
