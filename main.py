
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
                   "Laboratory": {"South": "Kitchen", "East": "Ammo Room", "item": "ChemicalX"},
                   "Ammo Room": {"West": "Laboratory", "item": "RayGun"},
                   "Storage": {"East": "Engine Room", "North": "Kitchen", "item": "Metal"},
                   "Command Room": {"East": "Kitchen", "item": "Radio"},
                   "Indoor Farm": {"North": "Cryo-Chamber", "item": "Potatoes"},
                   "Cryo-Chamber": {"South": "Indoor Farm", "item": "Cryo-nade"},
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
        if "item" in rooms[current_room].keys():
            item_in_room = rooms[current_room]["item"]
            print(f"You see a {item_in_room}")
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
                new_inventory, new_rooms = handle_pickup_item(input_command, inventory, rooms, current_room)
                inventory = new_inventory
                rooms = new_rooms
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


def handle_pickup_item(item: str, item_inventory: list, rooms: dict, current_room):
    temp_inv: list = item_inventory
    temp_rooms: dict = rooms
    for key, item_value in temp_rooms[current_room].items():

        if key == "item":
            if item == item_value:
                temp_inv.append(item_value)
                del temp_rooms[current_room]["item"]
                break
            else:
                print("this item is not valid")
    # print(temp_rooms, temp_inv)
    return temp_inv, temp_rooms


# main start command
if __name__ == '__main__':
    main()

