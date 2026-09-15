from colorama import Fore, Style
from colors import yellow, cyan, error
from guide import speak
from utils import ask

PLACE = Fore.MAGENTA + Style.BRIGHT + "Place" + Style.RESET_ALL

def enter():
    print()
    cyan("Enter?")
    print()

    cyan("1. Yes")
    cyan("2. Yes")
    print()

    answer = input("> ")

    # validates the choice
    while answer != "1" and answer != "2":
        error("Invalid choice.")
        answer = input("> ")


questions = {
    "1": {
        "question": "What is this place?",
        "response": "This place, let's call it Place."
    },
    "2": {
        "question": "Who are you?",
        "response": "I will be your guide."
    },
    "3": {
        "question": "How do you know my name?",
        "response": "ERROR: RESPONSE UNAVAILABLE."
    }
}


def first_choice(name):
    asked = []
    asking = True

    while asking and len(asked) < 3:
        print()
        cyan("What do you want to ask?")
        print()

        for number, question in questions.items():
            if number not in asked:
                cyan(f"{number}. {question['question']}")

        print()
        cyan("0. Nothing")
        print()

        answer = input("> ")

        # validate the choice
        while answer != "0" and answer not in questions:
            error("Invalid choice.")
            answer = input("> ")

        # player doesn't want to ask anything else
        if answer == "0":
            yellow(f"{name}: ...")
            asking = False

        else:
            asked.append(answer)

            yellow(f"{name}: {questions[answer]['question']}")
            ask()

            if answer == "1":
                print(questions[answer]["response"])
                speak(questions[answer]["response"])

            elif answer == "2":
                print(questions[answer]["response"])
                speak(questions[answer]["response"])

            elif answer == "3":
                error(questions[answer]["response"])
