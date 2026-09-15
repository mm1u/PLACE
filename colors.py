from colorama import Fore, Style, init
from utils import type_text

init()


# custom color functions for terminal output

def error(text):
    print(Fore.RED + text + Style.RESET_ALL)

def red(text):
    type_text(Fore.RED + Style.BRIGHT + text + Style.RESET_ALL)

def yellow(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)

def green(text):
    print(Fore.GREEN + text + Style.RESET_ALL)

def magenta(text):
    print(Fore.MAGENTA + Style.BRIGHT + text + Style.RESET_ALL)

def cyan(text):
    print(Fore.CYAN + text + Style.RESET_ALL)
