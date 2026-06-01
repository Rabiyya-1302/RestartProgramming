# -----------------------------
# DUNGEON MAP (GRAPH)
# -----------------------------

rooms = {
    "entrance": {
        "description": "You are at the dark entrance of the dungeon.",
        "north": "hallway",
        "item": None
    },

    "hallway": {
        "description": "A narrow hallway with torches on the walls.",
        "south": "entrance",
        "east": "armory",
        "north": "chamber",
        "item": "rusty_key"
    },

    "armory": {
        "description": "Old weapons are scattered everywhere.",
        "west": "hallway",
        "item": "sword"
    },

    "chamber": {
        "description": "A strange chamber with a locked door ahead.",
        "south": "hallway",
        "north": "treasure_room",
        "item": None
    },

    "treasure_room": {
        "description": "💰 You found the treasure room! You win!",
        "south": "chamber",
        "item": "gold"
    }
}

# -----------------------------
# GAME STATE
# -----------------------------

current_room = "entrance"
inventory = []

# -----------------------------
# GAME LOOP
# -----------------------------

print("=== DUNGEON GAME START ===")

while True:

    room = rooms[current_room]

    # Show room info
    print("\n----------------------")
    print("You are in:", current_room)
    print(room["description"])

    # Show item if available
    if room["item"]:
        print("You see:", room["item"])

    # Ask player action
    command = input("\nWhat do you want to do? (north/south/east/west, take, inventory, quit): ").lower()

    # -------------------------
    # MOVE LOGIC (GRAPH TRAVERSAL)
    # -------------------------

    if command in ["north", "south", "east", "west"]:
        if command in room:
            current_room = room[command]
        else:
            print("You can't go that way!")

    # -------------------------
    # PICK ITEM
    # -------------------------

    elif command == "take":
        if room["item"]:
            inventory.append(room["item"])
            print("You picked up:", room["item"])
            room["item"] = None
        else:
            print("Nothing to take here.")

    # -------------------------
    # INVENTORY
    # -------------------------

    elif command == "inventory":
        print("Your items:", inventory)

    # -------------------------
    # QUIT
    # -------------------------

    elif command == "quit":
        print("Game Over.")
        break

    else:
        print("Invalid command.")

    # -------------------------
    # WIN CONDITION
    # -------------------------

    if current_room == "treasure_room":
        print("\n🎉 YOU WIN THE GAME!")
        break