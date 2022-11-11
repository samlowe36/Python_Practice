is_started = False
player_entry = input("Enter 'help' for list of commands. Please enter a command: ")


while player_entry.upper() != "QUIT":

    if player_entry.upper() == "HELP":
        print("""
Start - to start the car
Stop - to stop the car
Quit - to exit the game""")
        player_entry = input("> ")
    elif player_entry.upper() == "START" and is_started == False:
        is_started = True
        print("Car started...ready to go!")
        player_entry = input("> ")
    elif player_entry.upper() == "START" and is_started == True:
        print("Car already started!")
        player_entry = input("> ")
    elif player_entry.upper() == "STOP" and is_started == True:
       is_started = False
       print("Car stopped.")
       player_entry = input("> ")
    elif player_entry.upper() == "STOP" and is_started == False:
        print("Car already stopped!")
        player_entry = input("> ")
    elif player_entry.upper() == "QUIT":
        break
    else:
        print("I don't understand that")
        player_entry = input("> ")
print("Game Over. Thanks for playing!")
