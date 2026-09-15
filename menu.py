from colors import green, magenta, red
from game import game
import pyfiglet

# displays the PLACE title
def show_title():
    game_title = pyfiglet.figlet_format("PLAC E", font ='banner3')

    magenta(game_title)


# displays the game instructions
def instructions():
    green("───────────────────INSTRUCTIONS───────────────────")
    green("       Press Enter after each line of text.       ")
    green("   Type the number corresponding to your choice.  ")
    green("                 Type 0 to leave.                 ")
    green("──────────────────────────────────────────────────")


# keeps the menu active until the player starts or exits the game
def menu():

    show_title()

    menu_active = True

    while menu_active:
        print()
        print("╔═══════════════════════════════════════════════╗")
        print("║                      MENU                     ║")
        print("║═══════════════════════════════════════════════║")
        print("║                Type 1 to start.               ║")
        print("║                Type 0 to exit.                ║")
        print("╚═══════════════════════════════════════════════╝")
        print()
        print("          Enter confirms your choice.           ")
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