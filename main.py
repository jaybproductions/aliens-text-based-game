
# construct dict with rooms, items, and directions
# validate input
# move between rooms
# gather items and update inventory
# end game lose if enter alien room before all items
# win if all items have been collected

def main():
    # initialize inventory and rooms
    # still need to properly add rooms and inventory
    rooms: dict = {"Kitchen": {"North": "Laboratory", "South": "Storage", "East": "Indoor Farm", "West": "Command Room"},
                   "Laboratory": {"South": "Kitchen", "East": "Ammo Room"},
                   "Ammo Room": {"West": "Laboratory"},
                   "Storage": {"East": "Engine Room", "North": "Kitchen"},
                   "Command Room": {"East": "Kitchen"},
                   "Indoor Farm": {"North": "Cryo-Chamber"},
                   "Cryo-Chamber": {"South": "Indoor Farm"},
                   }
    inventory: list = []

    # initialize starting room
    current_room: str = "Kitchen"
    # add a state variable for the main game loop
    running: bool = True

    # show instructions on start
    start_instructions()
    # main game loop
    while running:

        print(f"You're in the {current_room}.")
        print(f"Inventory: {inventory}")
        print("---------------")
        get_input: str = input("Enter Your Move: \n")

        try:
            input_prefix, input_command = validate_input(get_input)
            if input_prefix == 0:
                # this is go - handle change room validation
                current_room = change_room(input_command, rooms, current_room)
            elif input_prefix == 1:
                # this is get - handle inventory validation
                pass
            else:
                # handle invalid input
                print(input_command)
                # running = False
        except TypeError:
            print("Your command was not valid.")


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
def validate_input(user_input):
    try:
        # split the input into prefix and command
        input_list: list = user_input.split(' ')
        prefix: str = input_list[0]
        command: str = input_list[1]

        if prefix == "go":
            # construct a list of all valid direction commands
            valid_commands: list = ["North", "South", "East", "West"]
            if command not in valid_commands:
                return 2, "Not a valid direction."
            return 0, command
        elif prefix == "get":
            return 1, command

    except IndexError:
        return 2, "You only entered one command."


# once input has been validated, updated current room
def change_room(input_command: str, rooms: list, current_room: str):

    updated_room: str = current_room
    for direction, room in rooms[current_room].items():
        if direction == input_command:
            updated_room = room

    # if the room did not get updated, it wasn't valid
    if updated_room == current_room:
        print("You cannot go this way.")
    # return the updated room
    return updated_room


# main start command
if __name__ == '__main__':
    main()

