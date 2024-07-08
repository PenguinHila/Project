import random


def generate_number(game_difficulty):
    random_number = random.randint(0, int(game_difficulty))
    return random_number

def get_guess_from_user(game_difficulty):
    while True:
        try:
            user_number = int(input(f"Please enter your guessing from 0 to {game_difficulty}: "))
            if 0 <= user_number <= game_difficulty:
                print(f"The number you have chosen is: {user_number}")
                return user_number
            else:
                print(f"Number is out of range. Please enter a number from 0 to {game_difficulty}")
        except ValueError:
            print(f"Invalid input. Please enter a valid number from 0 to {game_difficulty}:")

def compare_results(random_number, user_number):
    if random_number == user_number:
        return True
    else:
        return False



def play(game_difficulty):
    # generate random number
    random_number = generate_number(game_difficulty)
    while True:
        # Ask user for his number
        user_number = get_guess_from_user(game_difficulty)
        # compare both numbers
        results = compare_results(random_number, user_number)

        if results:
            print(f"{results}. You win!")
            win = True
            return win
        else:
            print("False. Please try again.")
            continue

