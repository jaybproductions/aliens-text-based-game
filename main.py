
# Christopher Blair
# construct dict with rooms, items, and directions
# validate input
# move between rooms
# gather items and update inventory
# end game lose if enter alien room before all items
# win if all items have been collected

# this is to make it easier to read the main game loop
COMMAND_PREFIXES = {
    "GO": 0,
    "EXIT": -1,
    "GET": 1,
    "ERROR": 2
}


def main():
    # initialize inventory and rooms
    # still need to properly add rooms and inventory
    rooms: dict = {"Kitchen": {"North": "Laboratory", "South": "Storage", "East": "Indoor Farm", "West": "Command Room"},
                   "Laboratory": {"South": "Kitchen", "East": "Ammo Room", "item": "ChemicalX"},
                   "Ammo Room": {"West": "Laboratory", "item": "RayGun"},
                   "Storage": {"East": "Engine Room", "North": "Kitchen", "item": "Metal"},
                   "Command Room": {"East": "Kitchen", "item": "Radio"},
                   "Indoor Farm": {"North": "Cryo-Chamber", "item": "Potatoes"},
                   "Cryo-Chamber": {"South": "Indoor Farm", "West": "Kitchen", "item": "Cryo-nade"},
                   "Engine Room": {"item": "Alien" }
                   }
    inventory: list = [0, 1, 2, 3, 4]

    # initialize starting room
    current_room: str = "Kitchen"
    # add a state variable for the main game loop
    running: bool = True

    # show instructions on start
    start_instructions()
    # main game loop
    while running:

        if current_room == "Engine Room":
            # handle checking if won or lost here depending on if all items have been gathered.
            did_win = did_win_or_lose(inventory)
            running = False
            if did_win:
                print("Congrats, you defeated the alien!")
            else:
                print("The alien has eaten you! You lose.")
            break

        print(f"You're in the {current_room}.")
        # check if an item exists in the room and if so print it
        if "item" in rooms[current_room].keys():
            item_in_room = rooms[current_room]["item"]
            print(f"You see a {item_in_room}")
        # print current inventory
        print(f"Inventory: {inventory}")
        print("---------------")
        # gather user input
        get_input: str = input("Enter Your Move: \n")

        try:
            # assign validate input tuple to prefix and command
            input_prefix, input_command = validate_input(get_input)
            # first check if the player wants to exit game
            if input_prefix == COMMAND_PREFIXES["EXIT"]:
                print("exiting Game")
                running = False
                break
                # check if the input command corresponds with a go command
            if input_prefix == COMMAND_PREFIXES["GO"]:
                # this is go - handle change room validation
                # change room function, returns the new current room
                current_room = change_room(input_command, rooms, current_room)
                # check if input corresponds to the get command
            elif input_prefix == COMMAND_PREFIXES["GET"]:
                # this is get - handle inventory validation
                # handle pickup items returns a new inventory with the item, and the new rooms dict without item
                new_inventory, new_rooms = handle_pickup_item(input_command, inventory, rooms, current_room)
                # setting the new inventory and the new rooms
                inventory = new_inventory
                rooms = new_rooms
            else:
                # handle invalid input
                print(input_command)
                # running = False
        # if both the prefix and the command was invalid, we throw this error
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
    if user_input == "exit":
        return COMMAND_PREFIXES["EXIT"], "exiting"
    try:
        # split the input into prefix and command
        input_list: list = user_input.split(' ')
        prefix: str = input_list[0]
        command: str = input_list[1]
        # if the command prefix is go, handle checking for valid rooms in the command
        if prefix == "go":
            # construct a list of all valid direction commands
            valid_commands: list = ["NORTH", "SOUTH", "EAST", "WEST"]
            if command.upper() not in valid_commands:
                return COMMAND_PREFIXES["ERROR"], "Not a valid direction."
            return COMMAND_PREFIXES["GO"], command
        # if the prefix is get
        elif prefix == "get":
            return COMMAND_PREFIXES["GET"], command
    # if the input was not an exit command and was only 1 in length, we need to throw an error.
    except IndexError:
        return COMMAND_PREFIXES["ERROR"], "You only entered one command."


# once input has been validated, updated current room
def change_room(input_command: str, rooms: dict, current_room: str):

    updated_room: str = current_room
    # loop through the key, value pairs of the current_room only
    for direction, room in rooms[current_room].items():
        # check if the direction exists that is the input command
        if direction.upper() == input_command.upper():
            updated_room = room

    # if the room did not get updated, it wasn't valid
    if updated_room == current_room:
        print("You cannot go this way.")
    # return the updated room / if the input was invalid it just returns the current_room
    return updated_room


def handle_pickup_item(item: str, item_inventory: list, rooms: dict, current_room):
    # create a copy of the current inventory
    temp_inv: list = item_inventory[:]
    temp_rooms: dict = rooms
    # loop through the key, value pairs in the current_room
    for key, item_value in temp_rooms[current_room].items():
        # if the key is the item key
        if key == "item":
            # check if the item command is the same as the item value in the current_room
            if item == item_value:
                # append the item to the inventory
                temp_inv.append(item_value)
                # remove the item from the room dict so it cant be used again
                del temp_rooms[current_room]["item"]
                break
            else:
                # if the item isnt in the room it isn't valid
                print("this item is not valid")
    # print(temp_rooms, temp_inv)
    # return the new list and the new rooms dict
    return temp_inv, temp_rooms


def did_win_or_lose(inventory):
    if len(inventory) == 6:
        return True
    return False


# main start command
if __name__ == '__main__':
    main()

