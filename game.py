from tkinter import messagebox
from colorama import Fore, Style
from color import red, yellow
from ascii import eye

PLACE = Fore.MAGENTA + "Place" + Style.RESET_ALL

def ask(): 
    choice = input("> ") 

    if choice == "0": 
        print("Goodbye!") 
        raise SystemExit 
    
    return choice

def game():
    name = input("Enter your name: ")

    messagebox.showinfo(
    "SYSTEM",
    f"We know you, {name}."
    )

    print()
    print("You are awake.")
    ask()
    print("But are you REALLY awake?")
    ask()
    eye()
    ask()
    red("Something is watching you...")
    ask()
    yellow(f"{name}: Where am I?")
    ask()
    yellow(f"{name}: What is this place?")
    ask()
    yellow(f"{name}: Who are you?")
    ask()
    print("Too many questions.")
    ask()
    print(f"This place, let's call it {PLACE}.")
    ask()
    print("I will be your guide.")

    messagebox.showwarning(
    "SYSTEM",
    "Don't listen to it."
    )

    ask()
    yellow(f"{name}: ???")
    ask()
    yellow(f"{name}: What was that?")
    ask()
    print("What was what?")
    ask()
    print("I am here to help you.")

