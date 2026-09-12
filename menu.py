from color import blue, green
from game import game

def instructions():
    green("------------------INSTRUCTIONS------------------")
    green("Press Enter after each line of text.")
    green("Type the number corresponding to your choice.")
    green("------------------------------------------------")

def menu():
    menu_active = True

    while menu_active:
        blue("----------------------MENU----------------------")
        blue("                Type 1 to start                 ")
        blue("                Type 0 to exit                  ")
        blue("------------------------------------------------")

        choice = input("> ")

        if choice == "1":
            instructions()
            input("> ")
            game()
            menu_active = False

        elif choice == "0":
            print("Goodbye!")
            menu_active = False

        else:
            print("Invalid choice. Please enter 1 or 0.")