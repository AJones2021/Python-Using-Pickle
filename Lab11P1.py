# Anna Jones
# 08/12/2023
# Classes and OO Programming
#
import pickle
from inventory_item import InventoryItem

def main():
    inventory = load_inventory()
    display_inventory(inventory)

    answer = ''
    while answer.lower() != 'n':
        # TODO - Create an InventoryItem object, ask the user for item input
        #  using the object's method, then append the object to the inventory
        #  list.

        new_item = InventoryItem()
        new_item.get_item_input()
        if inventory is not None:
            inventory.append(new_item)
        answer = input('Do you want to enter more items? y/n')

    display_inventory(inventory)
    save_inventory(inventory)

def load_inventory():
    inventory = []
    # TODO - Attempt to load inventory data from a binary file named
    #  inventory.dat. If the file exists, load it into the inventory list.
    #  If the file does not exist, leave the inventory list empty.
    try:
        file = open('inventory.dat', 'rb')
        inventory = pickle.load(file)
        file.close()
    except:
        return inventory

def save_inventory(inventory):
    # TODO - Open a binary file named inventory.dat and dump the inventory
    #  list that has been passed in as a parameter to that file.
    file = open('inventory.dat', 'wb')
    pickle.dump(inventory, file)
    file.close()
    print('Inventory.dat file was created.')

def display_inventory(inventory):
    print()
    print('Current Inventory')
    print('-----------------')
    # TODO - Display the inventory items that are in the inventory list
    #  that was passed in as a parameter. If the list is empty, display
    #  "Inventory is empty."
    if len(inventory) == 0:
        print("Inventory is empty")
    else:
        for o in inventory:
            print(o)


main()
