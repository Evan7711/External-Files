#------------------------------------------------------------------------------
# Created By: Evan Smart
# Created On: 03/10/2023
# Version: 3.0
# Class: CS 30
# Assignment: Map RPG
#------------------------------------------------------------------------------
"""
Runs a continuous rpg where you can move around a map and search for items
"""
#------------------------------------------------------------------------------
import Movement
import Search
import Map
# Global variables for column and row
# Formats the map in rows and columns

#Nested Dictionary for all inventory items
Objects = {"Gun":
          {"Description": "A weapon that does 45 damage"},
          "MedKit":
          {"Description": "A kit that can heal 30 health"},
          "Knife":
          {"Description": "A weapon that does 20 damage"},
          "Food":
          {"Description": "A meal that can heal 10 health"}
          }
Ship_keys = ("PirateTile", "NothingTile", "StorageTile", "EscapeTile", "DeckTile", "WheelHouseTile", "StartTile", "RoomTile", "BoilerTile")
Ship_tiles = {"PirateTile": 
              {"Description": "There are pirates in here"},
              "NothingTile": 
              {"Description":"You are in an empty room"},
              "StorageTile": 
              {"Description":"You are in a storage room",                   "Inventory": "[Food]"},
              "EscapeTile": 
              {"Description":"You've made it to the rafts"},
              "DeckTile": 
              {"Description":"You are on the Deck"},
              "WheelHouseTile":
              {"Description":"You are behind the wheel of the ship", "Inventory": "[Gun]"},
              "StartTile": 
              {"Description":"You are on the starting tile"},
              "RoomTile":
              {"Description":"You are in your room",                        "Inventory": "[MedKit]"},
              "BoilerTile": 
              {"Description":"You are in the boiler room",                  "Inventory": "[Knife]"}
             }



# Code to print players current location
while True:
    current_location = Map.Ship_map[Movement.row][Movement.column]
    if current_location in Ship_keys:
        print(Ship_tiles[current_location]["Description"])
    else:
        print("Something went wrong!")
 #Code for Main Menu
    choice = input("What would you like to do: Walk, Search, Check Inventory, Check Map, or Quit: ")
    if choice == "walk" or choice == "Walk":
        Movement.Movement()
    elif choice == "quit" or choice == "Quit":
        print("Thank you for playing")
        break
    elif choice == "search" or choice == "Search":
        Search.Look(current_location)
    elif choice == "Check Inventory" or choice == "check inventory":
        print(Search.Inventory)
    elif choice == "Check Map" or choice == "check map":
         print(Map.Ship_map)
    else:
        print("You can't do that")