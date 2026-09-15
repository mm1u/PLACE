from tkinter import messagebox
import os
import getpass
from colors import red, yellow
from eye import eye_animation
from door import door_animation
from guide import speak
from utils import ask
from choices import enter, first_choice


# gets the username of the current computer user
def get_computer_username():
    try:
        return getpass.getuser()
    except Exception:
        return os.environ.get("USER") or os.environ.get("USERNAME") or "Player"


# runs the main sequence of the game
def game():
    ask()

    enter()

    door_animation()

    pc_username = get_computer_username()

    messagebox.showinfo(
        "SYSTEM",
        f"We know you, {pc_username}."
    )

    print()
    print("You are awake.")
    ask()
    eye_animation()
    red("Something is watching you...")
    ask()
    print(f"Hello {pc_username}.")
    speak(f"Hello {pc_username}.")
    ask()
    first_choice(pc_username)
    ask()

    messagebox.showwarning(
        "SYSTEM",
        "Don't listen to it."
    )

    yellow(f"{pc_username}: ???")
    ask()
    yellow(f"{pc_username}: What was that?")
    ask()
    print("What was what?")
    speak("What was what?")
    ask()
    print("I am here to help you.")
    speak("I am here to help you.")
    ask()
    