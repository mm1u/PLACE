from colorama import Fore, Style, init

init()

def red(text):
    print(Fore.RED + text + Style.RESET_ALL)

def yellow(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)

def blue(text):
    print(Fore.BLUE + text + Style.RESET_ALL)

def green(text):
    print(Fore.GREEN + text + Style.RESET_ALL)
