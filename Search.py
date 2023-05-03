"""
This is my search file
"""
# Map layout of ship
Ship_map = [
  ["PirateTile", "NothingTile", "StorageTile", "EscapeTile"],
  ["NothingTile", "StorageTile", "DeckTile","WheelHouseTile"],
  ["StartTile", "PirateTile", "RoomTile", "StorageTile"],
  ["BoilerTile", "NothingTile", "PirateTile", "NothingTile"]
]
# Empty dictionary used to update inventory
Inventory = []
# Function containing all of the code for searching
def Look(current_location):
    """
    Allows user to look around the room
    """ 
    searching = True
    while searching:
        searching = False
        if current_location == "StorageTile":
            print("You've found some food")
            if "Food" not in Inventory:
                Inventory.append("Food")
            else:
                Food = (input("You've already got some food do you really need more? "))
                if Food.lower() == "yes":
                    Inventory.append("Food")
                elif Food.lower() == "no":
                    print("You leave the food behind")
                else:
                    print("That's not a valid response")
        elif current_location == "RoomTile":
            print("You've found a medkit")
            if "MedKit" not in Inventory:
                Inventory.append("MedKit")
            else:
                print("You already have a Medkit")
        elif current_location == "BoilerTile":
            print("You've found a knife")
            if "Knife" not in Inventory:
                Inventory.append("Knife")
            else:
                print("You only need one knife")
        elif current_location == "WheelHouseTile":
            print("You've found a gun")
            if "Gun" not in Inventory:
                Inventory.append("Gun")
            else:
                print("You already have a gun")
        else:
            print("There's nothing in here")