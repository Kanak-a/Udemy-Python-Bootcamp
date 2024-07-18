#Hangman program

import random
print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       """)
                   
print("Welcome to HANGMAN GAME! Have a fun time!")
                  
hangman = [ """ 
 ____
|/   |
|   
|        
|    
|    
|
|_____
=======
""" ,
"""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
=======
""",
"""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
=======
""",
"""
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____
=======
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
=======
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____
=======
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \
|
|_____
=======
""",
"""
 ____
|/   |
|   (_)
|   /|\
|    |
|   | |
|
|_____
=======
""" 
]
word_list = ['kristen', 'dakota', 'diana', 'natalie']
chosen_word = random.choice(word_list) #any random chosen word 
word_length = len(chosen_word)
print(f"Psssst, the solution is {chosen_word}.")
display = []
for letter in chosen_word:
    display.append("_")  #representing each letter to guess
    
lives = 8
count = 0
loop = True
while loop:
    guess = input("Guess a letter: ").lower()
    
    #for exchanging the blanks with the letters in the display list
    for position in range(0, word_length):
        if chosen_word[position] == guess:
            display[position] = guess
        else:
            continue
     
    
    if guess in chosen_word:
        print("That's right!")
        print(f" {' '.join(display)} ")
    else:
        print(hangman[count])
        count+=1
        lives-=1
        if lives == 0:
            print("No lives left!")
            print("----GAME OVER----")
            loop = False
    
    #winning condition
    if "_" not in display:
        print(f"You cracked it!! - word : {chosen_word}")
        print("You win!")
        loop = False