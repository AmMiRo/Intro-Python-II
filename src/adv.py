# Imports here
import textwrap
import site
from room import Room
from player import Player
from item import Item

# Declare all the rooms with items
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["food"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["sword", "shield"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["gold"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["armor"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),

    "secret": Room("Secret Chamber", """You've found the secret closet hidden in the
Treasure Chamber! There is a lone pedestal holding a book in the corner""", ["spell book"]),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room["treasure"].e_to = room["secret"]
room["secret"].w_to = room["treasure"]

# Declare items
items = {
    "sword": Item("sword", "is very sharp"),

    "armor": Item("armor", "is form fitting and makes your butt look great"),

    "shield": Item("shield", "is pretty heavy"),

    "food": Item("food", "is raw"),

    "gold": Item("gold", "is shiny"),

    "spell book": Item("spell book", "is in a language you don't understand")
}


player = Player(input("What is your name, adventurer?"), room["outside"], [])

print(f"\nHello, {player.name}! Your adventure starts now.")

while True:

    print(f"\n{player.current_room.name}:")

    print(player.current_room.description + "\n")

    cmd = input("What will you do? (enter help for options)\n").lower().split(" ")
    if len(cmd) == 1:

        cmd = cmd[0]

        if cmd == "q":
            print("\ngoodbye\n")
            exit()

        elif cmd in ["n", "s", "e", "w"] :
            player.move_self(cmd)

        elif cmd == "search":
            player.current_room.search_room()

        elif cmd == "inventory":
            player.get_inventory()
        
        elif cmd == "help":
            print("Try: n, s, e, or w to move.\nTry: search to find items.\nTry: inspect, get, drop, or inventory with items.\n")

        else:
            print("\nI don't understand that command.\n")

    elif len(cmd) == 2:

        item = cmd[1]

        if cmd[0] == "get":
            player.get_item(item)

        elif cmd[0] == "inspect":
            items[item].inspect_item(player, item)

        elif cmd[0] == "drop":
            player.drop_item(item)
            
    else:
        print("\nI don't understand that command.\n")