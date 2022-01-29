from CurrencyRouletteGame import play as cr_game
from GuessGame import play as gg_game
from MemoryGame import play as mg_game
from Score import add_score
from utils import Screen_cleaner

input_name= ""

def welcome(name):
    global input_name
    input_name= name

    return (f"Hello {name} and welcome to the World of games.\n"
          f"Here you can find many cool games to play.\n")


def load_game():
    #Validation arguments
    allowed_games= [1, 2, 3]
    allowed_difficult_levels = list(range(1,6))


    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
                           "2. Guess Game - guess a number and see if you chose the computer.\n"
                           "3. Currency Roulette - try and guess the value of a a random amount of USD in ILS.\n")

    #Receive the selected game
    while True:
        #Clean the screen with the imported clear screen function
        try:
            game = int(input("Please select game: "))
            if game in allowed_games:
                break
            else:
                print(f"{game} is a wrong option, this is the allowed game numbers {allowed_games}")
        except ValueError:
            print("Only Int numbers is allowed!")
        except Exception as e:
            print(e)
   #Receive the selected difficult level
    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if difficulty in allowed_difficult_levels:
                break
            else:
                print(f"{difficulty} is not valid option, valid difficult levels {allowed_difficult_levels}")
        except ValueError:
            print("Only Int numbers is allowed!")
        except Exception as e:
            print(e)

    #Just a little bit of space...
    print("\n\n")

    #Run the selected game.
    if game == 1:
        result= mg_game(difficulty)
    elif game == 2:
        result= gg_game(difficulty)
    elif game == 3:
        result= cr_game(difficulty)

    #Add the user score to the file
    add_score(result, difficulty, input_name)

