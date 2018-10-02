#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""
import string
import collections
from a1_support import is_word_english

__author__ = "Your name & student number here"

# Write your functions here
def encrypt_text():
    """Return 'str' which prompt the user to enter a plain english text
    Parameter:
       No parameter:
    Return:
        string(str): displays and prompt the user to enter text to be encrypted
        integer(int): an offset interge number
    Precondition:
        int: 1 <= offset_key <= 25. based on 26 letters in english alphabet
        string: a valid inglish language.
        """
    text = input('Please enter some text to encrypt: ')
    offset_key = int(input('Please enter a shift offset (1-25): ')

    encrypted_text = ' '

    for i in range(len(text)):




def main():
    """Return the choice,'e','d','a' and 'q' to be selected from  the selection.
    Parameters:
        No parameters: prompt the user to selected an option from the chois given.
    Return:
        string(str): ask the user to enter texts according to the choice given
    """
    print('Welcome to the simple encryption tool!\n') # the welcome message 
    choice_opt = input('e) Encrypt some text\nd) Decrypt some text\na) Automatic decrypt Englist text\nq) Quit\n> ') # choice_opt (choice option), a variable where the input is assign to, and each option is display on the next line.
    # if statements to test for the choice given so that the action is taken 
    if choice_opt == 'e':
        encrypt_text()  # if the condition is true, a function of encryption is envoked and executed
    elif choice_opt == 'd':
        decrypt_text() # if true the decryption function is called and executed.
    elif choice_opt == 'a': # an automatic decryption of english text is envoked and executed
        decrypt_english_text()
    else:
        print('Bye!') # the program quit and print out str
    # Add your main code here
    pass


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

