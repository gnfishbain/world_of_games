import os
import pathlib
from utils import SCORES_FILE_NAME

SCORES_FILE_NAME= os.path.join(pathlib.Path(__file__).parent, "Scores.txt")

POINTS_OF_WINNING = lambda difficulty: (difficulty*3)+5

# Read the file and check if the user is existed
def read_the_file():
    with open(SCORES_FILE_NAME, 'r') as file:
        lines = file.readlines()
    return lines

#Get the user score
def get_score(name):
    lines= read_the_file()

    for line in lines:
        split_line= line.split(",")
        if split_line[0].lower().strip() == name.lower().strip():
            return split_line[1]

    raise Exception(f"{name} is not exist in the ({SCORES_FILE_NAME}) file!")

#Add score (Points) to user
def add_score(result: bool, difficulty: int, input_name: str) -> None:
    score= POINTS_OF_WINNING(difficulty)

    def create_new_file():
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write("")
            file.close()

    #Check if the score file exist
    if not os.path.isfile(SCORES_FILE_NAME):
        create_new_file()

    if result:
        #Check if user exist already in the file
        for index, line in enumerate(read_the_file()):
            split_line= line.split(",")

            name= split_line[0]
            ex_score= int(split_line[1])

            if name.lower().strip() == input_name.lower().strip():
                lines= read_the_file()
                #Pop the current line values
                del lines[index]

                #Push new line
                lines.append(f"{name},{score+ex_score}\n")

                #Recreate the file
                create_new_file()

                with open(SCORES_FILE_NAME, 'a') as file:
                    for line in lines:
                        file.write(line)
                    file.close()

                return

        #Push the line into the file
        with open(SCORES_FILE_NAME, 'a') as file:
            file.write(f"{input_name.lower()},{score}\n")

def read_all_existed_users():
    return [user.split(",")[0] for user in read_the_file()]
