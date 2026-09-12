from tkinter import messagebox
from colorama import Fore, Style
from colors import red, yellow
from eye import eye_animation
from door import door_animation
from guide import speak

PLACE = Fore.MAGENTA + Style.BRIGHT + "Place" + Style.RESET_ALL

def ask(): 
    choice = input("> ") 

    if choice == "0": 
        print("Goodbye!") 
        raise SystemExit 
    
    return choice

def game():
    ask()

    door_animation()

    name = input("Enter your name: ")

    messagebox.showinfo(
    "SYSTEM",
    f"We know you, {name}."
    )

    print()
    print("You are awake.")
    ask()
    eye_animation()
    red("Something is watching you...")
    ask()
    print(f"Hello {name}.")
    speak(f"Hello {name}.")
    ask()
    yellow(f"{name}: Where am I?")
    ask()
    yellow(f"{name}: What is this place?")
    ask()
    yellow(f"{name}: Who are you?")
    ask()
    print("Too many questions.")
    speak("Too many questions.")
    ask()
    print(f"This place, let's call it {PLACE}.")
    speak("This place, let's call it Place.")
    ask()
    print("I will be your guide.")
    speak("I will be your guide.")

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
    speak("What was what?")
    ask()
    print("I am here to help you.")
    speak("I am here to help you.")
    ask()
    