from selenium import webdriver
from Score import read_all_existed_users as file_users
import sys

url= "http://127.0.0.1:5000"
#The driver support Chrome version 97.0
chrome_drive= "./drivers/chromedriver.exe"

def test_score_service(name=None):
    driver = webdriver.Chrome(chrome_drive)
    driver.get(f"{url}/{name}")

    #Validate the url by the title
    assert "Scores Game" in driver.title

    #Read score id that contain the score number
    elem = driver.find_element("id", "score")

    curr_score= int(elem.text)

    driver.close()

    print(f"Testing url ({url}) with name argument ({name}) - result: ({curr_score}).")
    if curr_score >= 1 and curr_score <= 1000:
        return True
    return False

def main_function_call(users=[], read_from_score_file=True):
    if read_from_score_file:
        users= file_users()

    for user in users:
        result= test_score_service(name=user)
        print(f"User {user} test result ({result})")

        if not result:
            sys.exit(-1)




main_function_call(users=[], read_from_score_file=True)