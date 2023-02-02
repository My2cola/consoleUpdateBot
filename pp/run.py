def process_command(command):
    if command == "/epic":
        from epicUpdates import amongus, FallGuys, fortnitePars, GenshinImpact, warface
        print("Welcome to the Epic Games Store!")
        # ...
    elif command == "/steam":
        from steam import apex, warzone2, bot
        print("Welcome to Steam!")
        # ...
    elif command == "/riot":
        from RiotUpdates import lolUpdates, parsVal
        print("Welcome to Riot Games!")
        # ...
    elif command == "/battleNet":
        from batltleNet import Hearthstone
        print("Welcome to Battle.net!")
        # ...
    elif command == "/lesta":
        from lesta import wordOfTanks
        print("Welcome to Lesta Studios!")
        # ...
    elif command == "/help":
        # code to handle "/help" command
        print("Available commands: /epic, /steam, /riot, /battleNet, /lesta, /help")
        # ...
    else:
        # code to handle unknown commands
        print("Unknown command. Type /help for available commands.")
        # ...

while True:
    user_input = input("Enter a command: ")
    process_command(user_input)

