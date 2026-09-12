from colors import yellow, green, magenta, red
from game import game
import pyfiglet

def show_title():
    game_title = pyfiglet.figlet_format("PLAC E", font ='banner3')

    magenta(game_title)

def instructions():
    green("───────────────────INSTRUCTIONS───────────────────")
    green("       Press Enter after each line of text.       ")
    green("   Type the number corresponding to your choice.  ")
    green("                 Type 0 to leave.                 ")
    green("──────────────────────────────────────────────────")

def menu():

    show_title()

    menu_active = True

    while menu_active:
        print()
        yellow("╔═══════════════════════════════════════════════╗")
        yellow("║                      MENU                     ║")
        yellow("║═══════════════════════════════════════════════║")
        yellow("║                Type 1 to start.               ║")
        yellow("║                Type 0 to exit.                ║")
        yellow("╚═══════════════════════════════════════════════╝")
        print()
        yellow("          Enter confirms your choice.           ")
        print()

        choice = input("> ")

        if choice == "1":
            instructions()
            game()
            menu_active = False

        elif choice == "0":
            print("Goodbye!")
            menu_active = False

        else:
            red("Invalid choice. Please enter 1 or 0.")