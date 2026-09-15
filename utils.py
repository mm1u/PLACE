import time


# waits for the player's input; 0 exits the game
def ask(): 
    choice = input("> ") 

    if choice == "0": 
        print("Goodbye!") 
        raise SystemExit 
    
    return choice


# text appears character-by-character
def type_text(text, color="", delay=0.1):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)

    print()