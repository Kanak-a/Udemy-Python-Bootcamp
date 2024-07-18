from game_data import data
from higher_lower_ascii import art
import random

def details (account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}."
def draw_box(content, width=40):
    """Prints a box with centered content."""
    border = "+" + "-" * (width - 2) + "+"
    print(border)
    print(f"|{content.center(width - 2)}|")
    print(border)

#main
print(art)
print("Welcome to the Higher Lower game!")

account_b = random.choice(data)
score = 0
game = True

while game:
    account_a = account_b
    account_b = random.choice(data)

    print("---------------------------------------------------------")
    print("\n")
    print("A: ", details(account_a))
    print("\t\t---- vs ----\t\t")
    print("B: ", details(account_b))
    print("\n")
    print("----------------------------------------------------------")

    if account_a == account_b:
        account_b = random.choice(data)


    guess = input("Who has more followers? Type 'A' or 'B': ")
    if guess == 'A':
        if account_a['follower_count'] > account_b ['follower_count']:
            print("You are right!")
            score += 1
            draw_box(f"Current Score: {score}")
        else:
            print("You lose! Current Score: ", score)
            game = False

    else:
        if account_a['follower_count'] < account_b ['follower_count']:
            print("You are right!")
            score += 1
            print("Current Score: ", score)
        else:
            print("You lose! Current Score: ", score)
            game = False