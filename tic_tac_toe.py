from play_board import board
from colorama import Fore, Back, Style, Cursor


board()

user1 = 'O'
user2 = 'X'
print(
    "User 1 plays O, User 2 plays X. \n \
     User 1 starts. \n Use w,s,a,d to move, \n \
     enter to confirm")

"""colorama module allow me to play with
    colours of an otput in terminal. BACK - 
    background colour, FORE - font colore. RESET to remove all 
    efects.
    Available colours: BLACK, WHITE, RED, 
    BLUE, YELLOW, GREEN, MAGENTA, CYAN, 
    LIGHTBLACK_EX, LIGHTRED_EX, 
    LIGHTGEEN_EX, LIGHTYELLOW_EX, 
    LIGHTBLUE_EX, LIGHTMAGENTA_EX,
    LIGHTCYAN_EX, LIGHTWHITE_EX.
    """
print(Fore.RESET + Back.RESET + Style.DIM + Cursor.FORWARD + "User 1")

