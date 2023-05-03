"""
This is my movement file
"""
# import Map
row = 2
column = 0
# current_location = Map.Ship_map[row][column]
def Movement():
    """
    Allows user to move around
    """
    global row, column
    while True:
        Direction = input("Would you like to travel North, South, East, West: ")
        if Direction == "north" or Direction == "North":
            if row > 0:
                row -= 1
                break
            else:
                print("you can't go that way")
        elif Direction == "south" or Direction == "South":
            if row < 3:
                row += 1
                break
            else:
                print("you can't go that way")
        elif Direction == "east" or Direction == "East":
            if column < 3:
                column += 1
                break
            else:
                print("you can't go that way")
        elif Direction == "west" or Direction == "West":
            if column > 0:
                column -= 1
                break
            else:
                print("you can't go that way")
        else:
            print("You can't do that")