# This file contains the Currency Roulette game logic.

import requests
import random

def get_money_interval(difficulty_level, from_currency, to_currency):
    try:
        url = f'https://v6.exchangerate-api.com/v6/e2cce35ea4f3b261be89eb88/latest/USD'
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            raise Exception("Error: API request unsuccessful.")

        if 'conversion_rates' not in data:
            raise Exception("Error: Conversion rates not found in the response.")

        # When all is ok -
        if to_currency in data['conversion_rates']:

            # Get the currency and the amount to caculate.
            rate = data['conversion_rates'][to_currency]
            print("Currency date finished downloading.")
            random_number = random.randint(1, 100)
            # print(f"Try and guess the currency for this amount : {random_number}")
            allowed_difference = 10 - int(difficulty_level)
            print(f"The error margin allowed is: {allowed_difference}.")
            converted_amount = random_number * rate
            return random_number, converted_amount, allowed_difference

        else:
            raise Exception(f"Error: Currency {to_currency} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
def get_guess_from_user(random_number):
    while True:
            user_guess = int(input(f"Please convert the following amount from USD to ILS {random_number}: "))
            if type(user_guess) == int:
                print(f"The number you have chosen is: {user_guess}")
                return user_guess
            else:
                print("Please enter a number.")
                continue

def compare_results(difficulty_level,from_currency, to_currency):
    random_number, converted_amount, allowed_difference = get_money_interval(difficulty_level,from_currency, to_currency)
    user_guess = get_guess_from_user(random_number)
    if random_number - user_guess <= allowed_difference:
        return True
    else:
        return False

def play(difficulty_level,from_currency, to_currency):
    results = compare_results(difficulty_level,from_currency, to_currency)
    while results:
        print("Congratulations! Your guess is within the allowed difference.")
        win = True
        return win
    else:
        print("You failed.")

