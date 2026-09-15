# waits for the player's input; 0 exits the game
def ask(): 
    choice = input("> ") 

    if choice == "0": 
        print("Goodbye!") 
        raise SystemExit 
    
    return choice