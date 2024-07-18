#CAESAR CIPHER 
print("""
      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                    
      
        """)


#trying to combine both the ecnrypt and decrypt functions together
#*** clever way ***
def caesar(start_text, shift_amount, caesar_direction):
   caesar_text = ""
   if caesar_direction.lower() == "decode":
       shift_amount *=-1
   for letter in start_text:
       position = alphabet.index(letter)
       new_position = position + shift_amount
       caesar_text += alphabet[new_position]
   
   print(f"Here's the {caesar_direction}d message: {caesar_text}")
           
    
    
"""def Encrypt(text, shift, alphabet):
    
    caesar_text = ""
    for letter in text:
        position = alphabet.index(letter) 
        new_position = position + shift
        caesar_text += alphabet[new_position]
    print("Encrypted message: ", caesar_text)       
    
def decrypt(text, shift, alphabet):
    for i in range(len(text)):
        for letter in alphabet:
            if text[i] == letter:
                decoded_letter_index = alphabet.index(letter) - shift
        print( alphabet[decoded_letter_index], end = "") """  
game_stop = False
while not game_stop:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                'r','s','t','u','v','w','x','y','z']
    direction = input("| Type encode to encrypt and decode to decrypt |  - ")
    text = input("Input the text: ")
    shift = int(input("Enter the shift number: ")) 
    
    caesar(start_text = text, shift_amount = shift, caesar_direction = direction)
    
    choice = input("Do you wish to continue [y / n]: ")
    if choice == "y":
        game_stop = False
    else:
        game_stop = True
        print("Hope you enjoyed encrypting and decrypting the messages! ")


