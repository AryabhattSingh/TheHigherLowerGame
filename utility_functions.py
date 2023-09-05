import os


def clear_screen():
    """This function clears the console"""
    os.system('cls')


def get_user_guess():
    """This function takes user guess input on who may have more Instagram followers among option A or B. It returns A
     or B decided by whatever user enters."""
    user_guess = ""
    while user_guess != "A" and user_guess != "B":
        user_guess = input("\nWho has more Instagram followers? Type 'A' or 'B' :").upper()
        if user_guess != "A" and user_guess != "B":
            print("\nKindly enter a valid option.")
    return user_guess
