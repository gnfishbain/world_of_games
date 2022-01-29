import time, os
from random import randint

def generated_sequence(Difficulty):
    generated_list= [randint(1, 101) for _ in range(1, Difficulty+1)]

    #Show the numbers
    print(f"generated list: {generated_list}")

    #Wait for a second
    time.sleep(0.7)

    #Clear the screen - This is the best way that I found for clean the screen, the os.system('cls') didn't clean my scrren
    print("\n"*150)


    return generated_list
def get_list_from_user(Difficulty):
    numbers= []
    counter= 1
    while counter != Difficulty+1:
        numbers.append(int(input(f"Please enter number, entered numbers: {numbers}: ")))
        #increase the counter
        counter+= 1

    return numbers

def is_list_equal(difficulty):
    generated_numbers= generated_sequence(difficulty)
    user_input_numbers= get_list_from_user(difficulty)

    if generated_numbers == user_input_numbers:
        print("Right!")
        return True
    else:
        print("Wrong!")
        return False

def play(difficulty):
    return is_list_equal(difficulty)

