
# construct dict with rooms, items, and directions
# validate input
# move between rooms
# gather items and update inventory
# end game lose if enter alien room before all items
# win if all items have been collected

def main():
    # initialize inventory and rooms
    rooms: dict = {"Kitchen": {"North": "Laboratory", "South": "Storage"}}
    inventory: dict = {}

    #initialize starting room
    current_room: str = "Kitchen"
    # add a state variable for the main game loop
    running: bool = True

    # show instructions on start
    start_instructions()
    # main game loop
    while running:
        get_input: str = input(f"Welcome, you are currently in the {current_room}: ")
        if get_input == "jacob":
            running = False


# display the instructions for the player upon start
def start_instructions():
    print("Welcome to Space.")
    print("Collect all the materials and weapons you need to destroy the alien "
          "and fix the ship")
    print("Move commands: go South, go North, go East, go West")
    print('Add to inventory: get "item name"\n')
    return 0


# check that first word is go or get, validate that they are
# going to a valid room or picking up a valid item
def validate_input(user_input, rooms):
    return 0


# once input has been validated, updated current room
def change_room(user_input, rooms, current_room):
    return 0


# main start command
if __name__ == '__main__':
    main()

