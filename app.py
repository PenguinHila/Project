# This file acts as the main menu and entry point for the games.

from memory_game import play as play_memory_game
from guess_game import play as play_guess_game
from currency_roulette_game import play as play_currency_roulette
from score import add_score as add_score_win

def welcome():
    user_name_input = input("Please Enter Your name: ")
    print(f"Hi {user_name_input} and welcome to the World of Games: The Epic Journey")
    return user_name_input


def start_play():
    game_list = [
        "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
        "Guess Game - guess a number and see if you chose like the computer.",
        "Currency Roulette - try and guess the value of a random amount of USD in ILS."
    ]
    amount_of_games = len(game_list)

    while True:
        user_game_select = input("""Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
        2. Guess Game - guess a number and see if you chose like the computer.
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS 
        Your choice: """)

        if user_game_select.isdigit() and 1 <= int(user_game_select) <= amount_of_games:
            user_game_select = int(user_game_select)
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 3.")

    while True:
        game_difficulty = input("Thank you for selecting the game, please select a difficulty of 1-5: ")

        if game_difficulty.isdigit() and 1 <= int(game_difficulty) <= 5:
            break
        else:
            print("Invalid difficulty level. Please select a number between 1 and 5.")

    print(f"You have selected {game_list[user_game_select - 1]} with Difficulty {game_difficulty}")
    return user_game_select, game_difficulty


def main_menu():
    # user_name = welcome()
    while True:
        user_game_select, game_difficulty = start_play()
        game_difficulty = int(game_difficulty)
        print(user_game_select)
        # Memory Game.
        if user_game_select == 1:
            win = play_memory_game(game_difficulty)

        # Guess Game
        elif user_game_select == 2:
            win = play_guess_game(game_difficulty)

        # Currency Roulette.
        elif user_game_select == 3:
            from_currency = 'USD'
            to_currency = 'ILS'
            win = play_currency_roulette(game_difficulty,from_currency, to_currency)

        if win == True:
            add_score_win(game_difficulty)


        play_again = input("Do you want to play another game? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! See you next time.")
            break  # Exit the loop and end the program

#
# if __name__ == "__main__":
#     main_menu()