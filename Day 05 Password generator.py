#Random password generator
import random

print("Welcome to random password generator! \nMake sure to generate a strong password using the program.")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '%', '&', '*', '+', '-', '.', '/',]

no_of_letters = int(input("How many letters do want: "))
no_of_symbols = int(input("How many symbols: "))
no_of_numbers = int(input("How many numbers: "))
#length = int(input("What lenght should it be: "))

#Easy level of password generation

password = ""
for i in range(no_of_letters):
    random_letter = random.choice(letters)
    password += random_letter
    
for i in range(no_of_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol
for i in range(no_of_numbers): 
    random_number = random.choice(numbers)
    password += random_number
password_list = list(password) #converting the str password into list
random_password = str(random.shuffle(password_list))
password = "".join(password_list)


print(f"Generated password is : {password}")



    