from random import randint

def get_money_interval(generated_number, difficulty):
    dollar_rate= 3.1
    total= generated_number * dollar_rate

    interval= (total - (5 - difficulty), total +(5 - difficulty))
    return interval

def get_guess_from_user(difficulty):
    generated_number = randint(1, 100)

    # Ask user to guess the number
    guess= float(input(f"Please guess how much is {generated_number}$ in NIS: "))
    interval= get_money_interval(generated_number, difficulty)

    if guess > interval[0] and guess < interval[1]:
        print(f"You right!, the interval is {interval}.")
        return True
    else:
        print(f"You wrong!, the interval is {interval}.")
        return False

def play(difficulty):
    return get_guess_from_user(difficulty)
