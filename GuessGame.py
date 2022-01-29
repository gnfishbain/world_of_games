from random import randint

def generate_number(difficulty):
    global secret_number
    secret_number= randint(1, difficulty)
    #print(f"The secret number is {secret_number}")
    return secret_number

def get_guess_from_user(difficulty):
    return int(input(f"Please enter a number between 1 to {difficulty}: "))

def compare_result(difficulty):
    result= generate_number(difficulty) == get_guess_from_user(difficulty)

    if result:
        print("Great! you guess the right number!")
    else:
        print(f"Wrong number, the right number was {secret_number}!")

    return result

def play(difficulty):
    return compare_result(difficulty)
