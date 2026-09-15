from tkinter import messagebox
from colors import red, yellow
from eye import eye_animation
from door import door_animation
from guide import speak
from utils import ask
from choices import enter, first_choice


# runs the main sequence of the game
def game():
    ask()
    
    enter()

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
    first_choice(name)
    ask()

    messagebox.showwarning(
        "SYSTEM",
        "Don't listen to it."
    )

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
    