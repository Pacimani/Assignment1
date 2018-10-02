#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""
import string
from a1_support import is_word_english


__author__ = "Imani Pacifique & 45217171"


KEY = 26  # this key and letters are constant hence, global variable, they can be used by any function
    # importing ascii lowercase and uppercase alphabet from str module
letter_up_case = string.ascii_uppercase 
letter_low_case = string.ascii_lowercase


def encrypt(text, offset):
    """An encrypt function which takes an text 'str' and an offset 'int' as input and returns a encrypt the text 'str'  as per the offset given. 

    Parameter:
       text(str): a valid plain text to be encrypted.
       offset(int): an integer offset of encryption.

    Returns:
       string (str):Returns the encrypted text based on the offset given.

    Precondition:
        offset(int): 1 <= offset_key <= 25. based on 26 letters in english alphabet.
        text(str): a text with characters present in classical latin alphabet. eg: French or Swahili use the same alphabet as english.
        """



    # a variable to store the encrypted character
    encrypted_text = ""   

    # looping over all character in text to be ecrypted
    for char in text:   
        if char in letter_low_case:
            encrypted_text += letter_low_case[(letter_low_case.index(char) + offset) % (len(letter_low_case))] # indexing char in the alphabet and add it to encrypted_text

        elif char in letter_up_case:
            encrypted_text += letter_up_case[(letter_up_case.index(char) + offset) % (len(letter_up_case))]
 
        else:   # any english or non-english character is added to the encrypted_text
            encrypted_text += char

    return encrypted_text
            
            

def encrypt_text():
    """Prompt the user to enter a text 'str' and an offset 'int' then returns an encrypted version of the original text iff an offset [1,25] is given.
            and an ascending sequence of offset[1,25](int)  and their respective encrypted text(str) iff a 0 offset is given


    Returns:
       string(str):encrypted text as per offset given.
             (int):ascending sequence of 'int' iff an offset of 0 is given
    
    Parameter:
       No parameter:
        
        """

    text_one = input('Please enter some text to encrypt: ')
    offset_key = int(input('Please enter a shift offset (1-25): '))

    if offset_key == 0:
    
        print('The encrypted text is:')

        # looping over numbers in the range of [1,25] iff off_key 'int' == 0
        for offset_key in range(1,KEY):
            encrypted_text = encrypt(text_one, offset_key) 
            print('  %s: %s' %('{:02}'.format(offset_key),encrypted_text))  

    # otherwise printing an encrypted text iff the user provides an offset 'int' 1<= offsets <= 25.
    else:
        encrypted_text = encrypt(text_one, offset_key)
        print('The encrypted text is:', encrypted_text) 
    



def decrypt(text, offset):
    """Takes text 'str' to be decrypted and offset 'int' 

    Returns:
        (str):the decrypted text as per the offset given.

    Parameter:
       text(str): a valid coded plain text to be decrypted.
       offset(int): an integer offset of decryption.
    Precondition:
        offset(int): 1 <= offset_key <= 25. which was used to encrypt the original text.
        text(str): a text with characters present in classical latin alphabet (26 letters).
        """

    return encrypt(text,-offset)




def decrypt_text():
    """Prompt the user to enter a text 'str' and an offset 'int' then returns a decrypted text iff an offset [1,25] is given.
            and an ascending sequence of offset[1,25](int)  and their respective decrypted text(str) iff a 0 offset is given


    Returns:
       string(str):decrypted text as per offset given.
             (int):ascending sequence of 'int' iff an offset of 0 is given
    
    Parameter:
       No parameter:
        
        """

 
    text_one = input('Please enter some text to decrypt: ')
    offset_key = int(input('Please enter a shift offset (1-25): '))

    if offset_key == 0:
        
        print('The decrypted text is: ')
        for offset_key in range(1,KEY):

            # calling decrypt function and assign the return text to decrypted_text
            decrypted_text = decrypt(text_one, offset_key) 
            print('  %s: %s' %('{:02}'.format(offset_key),decrypted_text))

    else:   # otherwise printing an decrypted text iff the user provides an offset 'int' 1<= offsets <= 25.
        decrypted_text = decrypt(text_one, offset_key) 
        print('The decrypted text is:', decrypted_text)




def find_encryption_offsets(encrypted_text):
    """A function which takes an encrypted text and return a tuple of possible offsets used to encrypt the words in the text

    Returns:
       tuple of int: a tuple offset of positive integer  used to encrypt the text or an emply tuple if the the encrypted text has no valid words .

    Parameter:
       encypted_text (str): the encrypted text to check its offset

    """
    
    possible_offsets = [] # a list to store the possible offsets
    
    for offset_key in range(1,KEY):
        decrypted = decrypt(encrypted_text, offset_key)
        words = decrypted.replace('-', ' ').split(' ')
        
        is_valid = True
        
        for word in words:
            if "'" in word: #iff there is "'" in the word, the loop continues
                continue
            
            new_word = ""
            
            for char in word:

                #checking whether there is alphebetic character  char 'str' in word
                if char.isalpha():  
                    new_word += char # new word in the loop

            if not is_word_english(new_word.lower()): # checking if it is an english word
                is_valid = False
                break                       
            
        if is_valid:
            possible_offsets.append(offset_key)
            
    return tuple(possible_offsets)


def decrypt_englist_text():
    """An automatic decrypt function which uses all possible offsets 1<= offsets <= 26 to decrypt a text. then returns a sequence of offsets 'int' iff
    the decrypted text has more than one offset, otherwise returns the decrypted text 'str' and its offset 'int'

    Returns:
    (str) and (int):Returns a decrypted text 'str' and an offset 'int' iff the text has one offset.
             (int):Returns  sequence of offsets 'int' iff the the decrypted has multiple offset of encryption
              (str):Returns a string 'str' iff the text has no valid words

    Parameter:
       No parameter:
        
        """

    text_one = input('Please enter some encrypted text: ')

    possible_offsets = find_encryption_offsets(text_one) # finding text_one  offset

    if len(possible_offsets) > 1:
        
        # iff there is more than one item int the possible_offset 'tuple' we slice it to print the sequence of offsets 'int'
        print('Multiple encryption offsets:',str(possible_offsets)[1:-1])
        
    elif len(possible_offsets) == 1:
        
        # iff the possible encryption in one element in the tuple, we use the it to decrypt the text.
        print('Encryption offset:', str(possible_offsets[0]) + '\nDecrypted message:',decrypt(text_one,possible_offsets[0]))

    else:    # otherwise, this is printed iff the tuple in empty.
        print('No valid encryption offset')



def main():
    """The main function which envokes other functions. Hence, creates interactive interface between the user and the program.
    Return the choice,str('e','d','a' and 'q')  to be selected from.
    """
    print('Welcome to the simple encryption tool!') 


    while True:
        choice_option = input('\nPlease choose an option [e/d/a/q]:\n  e) Encrypt some text\n  d) Decrypt some text\n  a) Automatically decrypt English text\n  q) Quit\n> ')

        # iff choice_option = 'e' the function of encryption is envoked and executed
        if choice_option == 'e':
            encrypt_text()  

        # iff choice_option = 'd' the decryption function is called and executed.
        elif choice_option == 'd':
            decrypt_text() 

        # iff choice_option = 'a' the decryption function is called and executed.        
        elif choice_option == 'a': 
            decrypt_englist_text()

         # iff choice_option = 'q' the loop is broken. 
        elif choice_option == 'q':
            print('Bye!')
            break
        
        else:
             print('Invalid command')



    


##################################################
# !! Do not change (or add to) the code below !! #
#
# This code will run the main function if you use
# Run -> Run Module  (F5)
# Because of this, a "stub" definition has been
# supplied for main above so that you won't get a
# NameError when you are writing and testing your
# other functions. When you are ready please
# change the definition of main above.
###################################################

if __name__ == '__main__':
    main()

