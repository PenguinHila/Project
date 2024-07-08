# Memory Game.
from utils import clear_terminal
import random
import time
import os


# Clears the screen after showing the numbers.
def clear_terminal():
    # Clear the terminal in a cross-platform way
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Mac and Linux
        os.system('clear')

def generate_sequence(game_difficulty):
    random_list = []
    for _ in range(game_difficulty):
        random_number = random.randint(1, 100)
        print(random_number, end=' ')
        random_list.append(random_number)
    print("\n")
    time.sleep(1)
    clear_terminal()
    return random_list

def get_list_from_user():
    while True:
        try:
            user_input = input("Please insert the showed numbers, separated by commas: ")
            user_list = user_input.split(',')
            user_list = [int(i) for i in user_list]
            return user_list
        except ValueError:
            print("Invalid input. please only enter numbers separated by commas")

def is_list_equal(user_list,random_list):
    if user_list == random_list:
        return True
    else:
        return False


def play(game_difficulty):
    # Show the random number to the user
    random_list = generate_sequence(game_difficulty)
    while True:
        # Request the input from the user
        user_list = get_list_from_user()
        # Check if it's equal
        results = is_list_equal(random_list, user_list)
        if results:
            print(f"Correct. You win!")
            win = True
            return win
        else:
            print("Wrong. Please try again.")
            continue


