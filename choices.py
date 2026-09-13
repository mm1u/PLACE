from colorama import Fore, Style
from colors import yellow, cyan, red
from guide import speak
from utils import ask

PLACE = Fore.MAGENTA + Style.BRIGHT + "Place" + Style.RESET_ALL

def first_choice(name):
    # first question
    print()
    cyan("What do you want to ask?")
    print()

    cyan("1. What is this place?")
    cyan("2. Who are you?")
    print()

    # validate the first choice
    first_answer = input("> ")

    while first_answer != "1" and first_answer != "2":
        red("Invalid choice.")
        first_answer = input("> ")

    # player asks about the place
    if first_answer == "1":
        yellow(f"{name}: What is this place?")
        ask()

        print(f"This place, let's call it {PLACE}.")
        speak("This place, let's call it Place.")
        ask()

        # second question
        print()
        cyan("What else would you like to ask?")
        print()

        cyan("1. Who are you?")
        cyan("2. Nothing")
        print()

        # validate the second choice
        second_answer = input("> ")

        while second_answer != "1" and second_answer != "2":
            red("Invalid choice.")
            second_answer = input("> ")

        # player asks who the Guide is
        if second_answer == "1":
            yellow(f"{name}: Who are you?")
            ask()

            print("I will be your guide.")
            speak("I will be your guide.")

        # player doesn't want to ask anything else
        elif second_answer == "2":
            yellow(f"{name}: ...")

    # player asks who the Guide is
    elif first_answer == "2":
        yellow(f"{name}: Who are you?")
        ask()

        print("I will be your guide.")
        speak("I will be your guide.")
        ask()

        # second question
        print()
        cyan("What else would you like to ask?")
        print()

        cyan("1. What is this place?")
        cyan("2. Nothing")
        print()

        # validate the second choice
        second_answer = input("> ")

        while second_answer != "1" and second_answer != "2":
            red("Invalid choice.")
            second_answer = input("> ")

        # player asks about the place
        if second_answer == "1":
            yellow(f"{name}: What is this place?")
            ask()

            print(f"This place, let's call it {PLACE}.")
            speak("This place, let's call it Place.")

        # player doesn't want to ask anything else
        elif second_answer == "2":
            yellow(f"{name}: ...")
