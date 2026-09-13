def ask(): 
    choice = input("> ") 

    if choice == "0": 
        print("Goodbye!") 
        raise SystemExit 
    
    return choice